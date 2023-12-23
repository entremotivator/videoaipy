import streamlit as st
from moviepy.editor import VideoFileClip
import os

# Sidebar file uploader
files = st.sidebar.file_uploader('File uploader', accept_multiple_files=True, type=['mp4'])

# Temporary directory to save uploaded videos
temp_dir = 'temp_videos'
os.makedirs(temp_dir, exist_ok=True)

# Function to process each uploaded video
def process_video(file):
    video_path = os.path.join(temp_dir, file.name)
    
    # Save the uploaded video to the temporary directory
    with open(video_path, 'wb') as f:
        f.write(file.read())

    # Load the video using VideoFileClip
    video_clip = VideoFileClip(video_path)

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
