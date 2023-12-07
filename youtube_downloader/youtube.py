from pytube import YouTube
import tkinter as tk #2d graphics library
from tkinter import filedialog

def download_video(url, save_path):

    try:
        yt = YouTube(url)
        # get all diff streams then select high resolution
        streams = yt.streams.filter(progressive = True, file_extension="mp4")
        highest_res_stream =  streams.get_highest_resolution()
        highest_res_stream.download(output_path = save_path)
        print("Video dowload successful!")

    except Exception as e:
        print(e)


url = "https://www.youtube.com/watch?v=494e4txpwSg"
save_path = "C:/Users/rajee/OneDrive/Documents/rtdatasci_github/Python/youtube_downloader"

download_video(url, save_path)



## test pytube in terminal:
#pytube "https://www.youtube.com/watch?v=494e4txpwSg"