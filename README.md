## YouTube Video Generator
Generates high quality YouTube videos in WebM format

[Demonstration (Windows)](Demonstration.webm)
## Description
```python
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
```
## Dependency Check
---
|Windows|
|-------|
```powershell
python --version
```
```powershell
pytube --version
```
```powershell
ffmpeg -version | Select-Object -First 1
```
---
|Linux|
|-----|
```bash
python --version
```
```bash
pytube --version || pip show pytube | grep "Version"
```
```bash
ffmpeg -version | head -n 1
```
