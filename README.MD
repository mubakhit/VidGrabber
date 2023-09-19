# Video Downloader and Converter

This script is designed to help you download and convert videos from YouTube and other supported websites using `yt-dlp` and `ffmpeg`. It provides a simple way to manage a list of video URLs and their associated names. Additionally, it keeps a history of your downloads in a JSON file.

## Getting Started

Before running the script, make sure you have the following prerequisites:

1. **Python**: You should have Python installed on your computer. You can download it from the official Python website: [python.org](https://www.python.org/downloads/).

2. **yt-dlp and ffmpeg**: You need to download `yt-dlp` and `ffmpeg` and place their executable files in the same directory where you intend to run this script. You can find `yt-dlp` at [yt-dlp GitHub repository] Choose the `exe` file from releases (https://github.com/yt-dlp/yt-dlp) and `ffmpeg` at [ffmpeg.org](https://www.ffmpeg.org/download.html).

## First-Time Setup

When you run the script for the first time, it will create the following files and directory:

- **urls.txt**: This is the file where you should input the URLs of the videos you want to download, along with their associated names. The format should be as follows for example:
  `https://www.youtube.com/watch?v=QohH89Eu5iM "VideoName"`
  if you got **error** format try remove white spaces from the name.

- **History.json**: This JSON file stores a record of all the videos you have downloaded, including their names, download dates, and original URLs.

- **Downloads**: This directory will be created to store the downloaded video files.

## How to Use

1. Edit the `urls.txt` file with the video URLs you want to download and their associated names, as described above.

2. Place the `yt-dlp` and `ffmpeg` executable files in the same directory as this script.

3. Run the script by executing it using Python: `python VidGrabber.py`

## Notes

- If the script encounters an invalid line in the `urls.txt` file, it will skip that line and continue with the next one.

- You can rerun the script at any time to download additional videos. The script will not overwrite existing videos in the "Downloads" directory.

- The download history is maintained in the `History.json` file, so you can keep track of your downloads.

## Screenshots
