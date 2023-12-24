# Whisper Converter

This script automates the conversion of audio files from `.ogg` to `.mp3` format and then transcribes them into text files using the Whisper model. It is designed to handle batches of audio files efficiently, organizing the output into date-stamped folders.

## Features

- Converts `.ogg` files to `.mp3`.
- Transcribes `.mp3` files to `.txt` using OpenAI's Whisper model.
- Organizes files into date-stamped folders.
- Logs progress and processing time.

## Prerequisites

Before running the script, you need to have Python installed on your system along with the FFmpeg utility. The script also requires several Python libraries, which are listed in `requirements.txt`.

### Installing FFmpeg

FFmpeg is a free and open-source software project consisting of a large suite of libraries and programs for handling video, audio, and other multimedia files and streams. Installation instructions vary depending on your operating system:

#### On Windows

1. Download FFmpeg from [FFmpeg's official website](https://ffmpeg.org/download.html).
2. Unzip the downloaded file.
3. Add the path to `ffmpeg.exe` to your system's PATH environment variable.

#### On macOS

You can install FFmpeg using [Homebrew](https://brew.sh/):

```bash
brew install ffmpeg
```

#### On Linux

Most Linux distributions include FFmpeg by default. If not, you can install it using your package manager. For example, on Ubuntu:

```bash
sudo apt update
sudo apt install ffmpeg
```

### Python Libraries

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

The `requirements.txt` should contain:

```
whisper
pydub
tqdm
```

## Usage

To run the script, navigate to the script's directory in your terminal and execute:

```bash
python whisper_converter.py
```

Replace `whisper_converter.py` with the actual name of the script.

## Configuration

You can adjust the model size used for transcription by modifying the `MODEL_TYPE` variable in the script. Available options are `"base"`, `"medium"`, or `"large"`.

## Output

- Transcribed texts are saved in `.txt` files inside a folder named `txt` followed by the current date.
- The `.mp3` files are saved in a folder named `mp3` followed by the current date.

## Note

- The script disables SSL verification, which is not recommended for a production environment. This setting can be adjusted in the script if necessary.
- Ensure your audio files are compatible with the Whisper model for accurate transcription.
