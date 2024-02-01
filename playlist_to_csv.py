#!/mnt/data/projects/youtube_playlist_to_csv/.venv/bin/python
# a script to list down all videos of a youtube playlist with their duration in human readable format. This is helpful
# if you want to do a course from youtube and want to plan which vidoes to watch in upcoming days and set a target.
# written by chatgpt. Prompt given by : iamtalhaasghar
# 2024-02-01

import yt_dlp
import csv
from datetime import timedelta
import sys

def get_playlist_info(playlist_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        playlist_info = ydl.extract_info(playlist_url, download=False)

    return playlist_info

def format_duration(seconds):
    return str(timedelta(seconds=seconds))

def save_to_csv(playlist_info, output_file='playlist_info.csv'):
    with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Title', 'Duration', 'Human Readable Duration']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for entry in playlist_info['entries']:
            title = entry['title']
            duration = entry.get('duration', 0)
            human_readable_duration = format_duration(duration)
            writer.writerow({'Title': title, 'Duration': duration, 'Human Readable Duration': human_readable_duration})

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Kindly pass the youtube playlist link as well.')
        exit()
    playlist_url = sys.argv[1]
    playlist_info = get_playlist_info(playlist_url)
    save_to_csv(playlist_info)

