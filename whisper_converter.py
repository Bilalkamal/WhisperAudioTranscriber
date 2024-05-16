import os
import ssl
import whisper
import datetime
import time
from pydub import AudioSegment
from tqdm import tqdm

# "base" , "medium", or "large" ("tiny" not recommended for multilingual)
MODEL_TYPE = "medium"

def convert_ogg_to_mp3(source_directory):
    ogg_files = [f for f in os.listdir(source_directory) if f.endswith(".ogg")]
    for filename in tqdm(ogg_files, desc="Converting .ogg to .mp3"):
        ogg_audio = AudioSegment.from_ogg(filename)
        mp3_filename = f"{filename[:-4]}.mp3"
        ogg_audio.export(mp3_filename, format="mp3")
        os.remove(filename)

def convert_mp4_to_mp3(source_directory):
    mp4_files = [f for f in os.listdir(source_directory) if f.endswith(".mp4")]
    for filename in tqdm(mp4_files, desc="Converting .mp4 to .mp3"):
        mp4_audio = AudioSegment.from_file(filename,    "mp4")
        mp3_filename = f"{filename[:-4]}.mp3"
        mp4_audio.export(mp3_filename, format="mp3")
        os.remove(filename)

def convert_m4a_to_mp3(source_directory):
    m4a_files = [f for f in os.listdir(source_directory) if f.endswith(".m4a")]
    for filename in tqdm(m4a_files, desc="Converting .m4a to .mp3"):
        m4a_audio = AudioSegment.from_file(filename, "m4a")
        mp3_filename = f"{filename[:-4]}.mp3"
        m4a_audio.export(mp3_filename, format="mp3")
        os.remove(filename)  

def convert_wav_to_mp3(source_directory):
    wav_files = [f for f in os.listdir(source_directory) if f.endswith(".wav")]
    for filename in tqdm(wav_files, desc="Converting .wav to .mp3"):
        wav_audio = AudioSegment.from_file(filename, "wav")
        mp3_filename = f"{filename[:-4]}.mp3"
        wav_audio.export(mp3_filename, format="mp3")
        os.remove(filename)

        

def transcribe_audio(source_directory, model, mp3_directory, txt_directory):
    mp3_files = [f for f in os.listdir(source_directory) if f.endswith(".mp3")]
    all_texts = ""
    for filename in tqdm(mp3_files, desc="Transcribing .mp3 files"):
        print(f"Transcribing {filename}...")
        result = model.transcribe(filename, fp16=False)
        txt_filename = f"{filename[:-4]}.txt"

        with open(txt_filename, "w") as f:
            f.write(result["text"])

        all_texts += result["text"] + "\n"

        os.rename(filename, os.path.join(mp3_directory, filename))
        os.rename(txt_filename, os.path.join(txt_directory, txt_filename))

    return all_texts

def main():
    # Start the timer
    start_time = time.time()

    # Disable SSL verification (not recommended for production)
    ssl._create_default_https_context = ssl._create_unverified_context

    # Load Whisper model
    model = whisper.load_model(MODEL_TYPE)

    # Directories setup
    current_directory = os.getcwd()
    today = datetime.date.today().strftime("%Y-%m-%d")
    mp3_directory = os.path.join(current_directory, "mp3", today)
    txt_directory = os.path.join(current_directory, "txt", today)

    os.makedirs(mp3_directory, exist_ok=True)
    os.makedirs(txt_directory, exist_ok=True)

    # Convert .ogg to .mp3
    convert_ogg_to_mp3(current_directory)
    convert_mp4_to_mp3(current_directory)
    convert_m4a_to_mp3(current_directory)

    all_texts = transcribe_audio(current_directory, model, mp3_directory, txt_directory)

    print("Transcribed Texts:")
    print(all_texts)

    print(f"The directory of the output .txt files: {txt_directory}")

    end_time = time.time()
    print(f"Process completed in {end_time - start_time:.2f} seconds.")
    for _ in range(3):
        os.system("afplay /System/Library/Sounds/Submarine.aiff")

if __name__ == "__main__":
    main()
