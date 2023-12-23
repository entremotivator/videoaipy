import streamlit as st
from moviepy.editor import VideoFileClip

files = st.sidebar.file_uploader('File uploader', accept_multiple_files=True, type=['mp4'])

for f in files:
      video = VideoFileClip(f)    # This  gives an error!!!
