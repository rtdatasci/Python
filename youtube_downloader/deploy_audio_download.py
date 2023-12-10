from pytube import YouTube
from moviepy.editor import VideoFileClip
# import tkinter as tk #2d graphics library
# from tkinter import filedialog
import streamlit as st
import os


def download_audio(url, output_path):

    try:
        # Download video
        yt = YouTube(url)
        # ys = yt.streams.filter(only_audio=True).first()  # this option did not work becaue we need video fps metadata in later step
        ys = yt.streams.filter(file_extension='mp4').first()
        ys.download(output_path)

        # Convert to MP3 using moviepy
        video_path = output_path + "/" + ys.title + ".mp4"
        audio_path = output_path + "/" + ys.title + ".mp3"

        video = VideoFileClip(video_path)
        video.audio.write_audiofile(audio_path)

        # Remove the original video file
        video.close()
        os.remove(video_path)

        st.success(f"Download and conversion completed successfully!")
        st.info(f"The MP3 file is saved at: {audio_path}")
        st.audio(audio_path, format='audio/mp3')

    except Exception as e:
        st.text(f"An error occurred: {str(e)}")


# Streamlit UI
st.title("YouTube Video2audio converter")

# User input for YouTube URL
youtube_url = st.text_input("Enter YouTube URL:")
output_directory = st.text_input("Enter output directory (optional):")

if st.button("Convert youtube video2audio"):
    if youtube_url:
        # Set a default output directory if not provided
        output_directory = output_directory or "downloads"
        os.makedirs(output_directory, exist_ok=True)

        download_audio(youtube_url, output_directory)
    else:
        st.text("Please enter a valid YouTube URL.")


# deploy in bash
#streamlit run deploy_audio_download.py
