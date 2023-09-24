import subprocess

from custom_pytube_funcs import *

"""
---
Requests user for YouTube URL
---
Tries to find high quality video WebM streams
Tries to find high quality audio WebM streams
---
Downloads WebM video file in the format C:Users\Alex\Downloads\Video - {YouTube Title}
Downloads WebM audio file in the format C:Users\Alex\Downloads\Audio - {YouTube Title}
---
Uses FFmpeg (https://ffmpeg.org) to combine the video and audio into one file
---
User needs to have FFmpeg installed along with all other dependencies for the script to work
---
"""

directory = os.path.join(os.path.expanduser("~"), "Downloads")

youtube = YouTube(input("YouTube Link -> "))

video_itag = pick_video_stream(youtube)
audio_itag = pick_audio_stream(youtube)

if video_itag != 0 and audio_itag != 0:
    video_stream = youtube.streams.get_by_itag(video_itag)
    audio_stream = youtube.streams.get_by_itag(audio_itag)
    print(f"Selected Video Stream -> {video_stream_to_string(video_stream)}")
    print(f"Selected Audio Stream -> {audio_stream_to_string(audio_stream)}")
    video_path = download_video(video_stream, directory)
    audio_path = download_audio(audio_stream, directory)
    print(video_path)
    print(audio_path)
    dest_path = video_path.replace("Video - ", "Final - ")
    os.remove(dest_path) if os.path.exists(dest_path) else None
    ffmpeg_command = ["ffmpeg", "-i", audio_path, "-i", video_path, "-c:v", "copy", "-c:a", "copy", dest_path]
    subprocess.run(ffmpeg_command, stderr=subprocess.DEVNULL)
    print(dest_path) if os.path.exists(dest_path) else None
else:
    print("Unable to find high quality video/audio")
