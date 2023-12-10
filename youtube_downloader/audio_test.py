from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
import tkinter as tk #2d graphics library
from tkinter import filedialog

video_path = "C:/Users/rajee/OneDrive/Documents/rtdatasci_github/Python/youtube_downloader/Aashish.mp4"
audio_path = "C:/Users/rajee/OneDrive/Documents/rtdatasci_github/Python/youtube_downloader/Aashish.mp3"

video = VideoFileClip(video_path)
video.audio.write_audiofile(audio_path)

# Remove the original video file
video.close()
os.remove(video_path)


#pytube "https://www.youtube.com/watch?v=x-gGkfurIYI" -a