import os
import subprocess
import json
from datetime import datetime

# function to download videos using yt-dlp with 5 multi-threading
def download_video(url, output_dir, video_name):
    yt_dl_command = f'yt-dlp.exe -o "{output_dir}/{video_name}.%(ext)s" -f bestvideo+bestaudio/best --external-downloader aria2c --external-downloader-args "-x 5" --newline {url} >nul 2>&1'
    subprocess.call(yt_dl_command, shell=True)

# function to encode videos to mp4 using ffmpeg
def encode_to_mp4(input_file, output_file):
    ffmpeg_command = f'ffmpeg -i "{input_file}" -c:v libx264 -c:a aac "{output_file}" >nul 2>&1'
    subprocess.call(ffmpeg_command, shell=True)

# function to add a download entry to history file
def add_to_history(video_name, url):
    history_entry = {
        'Video Name': video_name,
        'Downloaded in': datetime.now().strftime('%d %b %Y'),
        'URL': url
    }

    history_file = 'History.json'
    if os.path.exists(history_file):
        with open(history_file, 'r') as file:
            history_data = json.load(file)
    else:
        history_data = []

    history_data.append(history_entry)

    with open(history_file, 'w') as file:
        json.dump(history_data, file, indent=4)

# Check if the 'urls.txt' file exists
if not os.path.isfile('urls.txt'):
    print('urls.txt file not found. Creating a new one.')
    with open('urls.txt', 'w') as file:
        pass  # Create an empty file

# Read the list of URLs and video names from a text file
with open('urls.txt', 'r') as file:
    lines = file.readlines()

# Check if the 'urls.txt' file is empty
if not lines:
    print('urls.txt file is empty.')
    exit()

# Create the "Downloads" directory if it doesn't exist
output_dir = 'Downloads'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through the URLs and download/encode each video
for idx, line in enumerate(lines, start=1):
    parts = line.strip().split(' ')
    if len(parts) != 2:
        print(f'Skipping line {idx}: Invalid format.')
        continue

    url, video_name = parts[0].strip(), parts[1].strip('"')
    print(f'Downloading video {video_name}...')
    download_video(url, output_dir, video_name)
    print(f'Video {video_name} downloaded.')

    # Add the download entry to History.json
    add_to_history(video_name, url)

# Encode all the downloaded videos
for idx, line in enumerate(lines, start=1):
    parts = line.strip().split(' ')
    if len(parts) != 2:
        print(f'Skipping line {idx}: Invalid format.')
        continue

    video_name = parts[1].strip('"')
    input_file = os.path.join(output_dir, f'{video_name}.mkv')
    output_file = os.path.join(output_dir, f'{video_name}.mp4')
    print(f'Encoding video {video_name}...')
    encode_to_mp4(input_file, output_file)
    print(f'Video {video_name} encoded.')

print('All videos downloaded in "Downloads dir "')
