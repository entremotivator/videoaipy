import streamlit as st
from moviepy.editor import VideoFileClip
import os
from tempfile import NamedTemporaryFile

files = st.sidebar.file_uploader('File uploader', accept_multiple_files=True, type=['mp4'])

# Temporary directory to save uploaded videos
temp_dir = 'temp_videos'
os.makedirs(temp_dir, exist_ok=True)

# Function to process each uploaded video
def process_video(file):
    # Save the uploaded video to the temporary directory
    temp_video = NamedTemporaryFile(delete=False, dir=temp_dir, suffix='.mp4')
    temp_video_path = temp_video.name
    temp_video.write(file.read())
    temp_video.close()

    # Load the video using VideoFileClip
    video_clip = VideoFileClip(temp_video_path)

    # Process the video (add your custom processing logic here)
    # For example, you can get the duration of the video
    duration = video_clip.duration

    # Return the result or do further processing
    return duration

# Process each uploaded file
for file in files:
    duration = process_video(file)
    st.write(f"Video '{file.name}' duration: {duration} seconds")

# Cleanup: Remove temporary directory after processing
st.experimental_rerun()

# Note: The cleanup logic may vary depending on your use case
# In a production scenario, consider a more robust cleanup mechanism
