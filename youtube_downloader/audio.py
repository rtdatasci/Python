from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
import tkinter as tk #2d graphics library
from tkinter import filedialog

def download_audio(url, output_path):
    # Download video
    yt = YouTube(url)
    ys = yt.streams.filter(only_audio=True).first()
    ys.download(output_path)

    # Convert to MP3 using moviepy
    video_path = output_path + "/" + ys.title + ".mp4"
    audio_path = output_path + "/" + ys.title + ".mp3"

    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

    # Remove the original video file
    video.close()
    os.remove(video_path)

# where to save the file
def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder

if __name__ == "__main__":
    video_url = input("Please input youtube url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print(f"Started download...") 
        download_audio(video_url, save_dir)
    else:
        print(f"Invalid save location")  


## test pytube in terminal:
## download audio only in my4
#pytube "https://www.youtube.com/watch?v=x-gGkfurIYI" -a