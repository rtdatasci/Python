from pytube import YouTube
import tkinter as tk #2d graphics library
from tkinter import filedialog
import streamlit as st
import os


def download_video(url, save_path):

    try:
        yt = YouTube(url)
        # get all diff streams then select high resolution
        streams = yt.streams.filter(progressive = True, file_extension="mp4")
        highest_res_stream =  streams.get_highest_resolution()
        st.text("Downloading video...")
        highest_res_stream.download(output_path = save_path)

    except Exception as e:
        st.text(f"An error occurred: {str(e)}")


# Streamlit UI
st.title("YouTube Video downloader")

# User input for YouTube URL
youtube_url = st.text_input("Enter YouTube URL:")
output_directory = st.text_input("Enter output directory (optional):")

if st.button("Download youtube video"):
    if youtube_url:
        # Set a default output directory if not provided
        output_directory = output_directory or "downloads"
        os.makedirs(output_directory, exist_ok=True)

        download_video(youtube_url, output_directory)
    else:
        st.text("Please enter a valid YouTube URL.")


# deploy in bash
#streamlit run deploy_download.py




# url = "https://www.youtube.com/watch?v=494e4txpwSg"
# save_path = "C:/Users/rajee/OneDrive/Documents/rtdatasci_github/Python/youtube_downloader"
# download_video(url, save_path)



## test pytube in terminal:
#pytube "https://www.youtube.com/watch?v=494e4txpwSg"
## download audio only in my4
#pytube "https://www.youtube.com/watch?v=x-gGkfurIYI" -a