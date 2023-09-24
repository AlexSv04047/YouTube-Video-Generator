import os

from pytube import YouTube, Stream

"""
---
Custom pytube functions for run.py
---
"""


def video_stream_to_string(stream: Stream):
    return f"itag: {stream.itag} | Resolution: {stream.resolution} | FPS: {stream.fps}"


def audio_stream_to_string(stream: Stream):
    return f"itag: {stream.itag} | BitRate: {stream.abr}"


def pick_video_stream(youtube: YouTube):
    max_res, max_res_itag = 0, 0
    streams = youtube.streams.filter(subtype="webm", only_video=True)
    for stream in streams:
        res = int(stream.resolution[:-1])
        if res >= 1080 and res > max_res:
            max_res, max_res_itag = res, stream.itag
    return max_res_itag


def pick_audio_stream(youtube: YouTube):
    max_abr, max_abr_itag = 0, 0
    streams = youtube.streams.filter(subtype="webm", only_audio=True)
    for stream in streams:
        abr = int(stream.abr[:-4])
        if abr >= 96 and abr > max_abr:
            max_abr, max_abr_itag = abr, stream.itag
    return max_abr_itag


def download_video(stream: Stream, directory):
    stream.download(directory, filename_prefix="Video - ")
    return os.path.join(directory, "Video - " + stream.default_filename)


def download_audio(stream: Stream, directory):
    stream.download(directory, filename_prefix="Audio - ")
    return os.path.join(directory, "Audio - " + stream.default_filename)
