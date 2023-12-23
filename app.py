import streamlit as st
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, vfx

def edit_video(input_path, output_path, start_time, end_time, text, font_size=70, text_color='white', playback_speed=1.0, output_format="webm", text_position='center'):
    try:
        # Load video clip and extract subclip
        video = VideoFileClip(input_path).subclip(start_time, end_time)

        # Make the text clip
        txt_clip = (TextClip(text, fontsize=font_size, color=text_color, bg_color='transparent')
                    .set_position(text_position)
                    .with_duration(video.duration))

        # Composite video with text
        result = CompositeVideoClip([video, txt_clip])

        # Adjust playback speed
        result = result.fx(vfx.speedx, playback_speed)

        # Write the edited video to the output path
        result.write_videofile(output_path, codec=output_format, audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=True)

        return True
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return False

def display_video(file_path, message=""):
    if st.button("Play Video"):
        st.video(file_path)

def main():
    st.title("Video Editor App")

    uploaded_file = st.file_uploader("Upload a video file", type=["mp4"])

    if uploaded_file:
        st.subheader("Preview Uploaded Video:")
        display_video(uploaded_file)

        col1, col2 = st.beta_columns([2, 1])
        with col1:
            start_time, end_time = st.slider("Select time range (seconds)", 0.0, 60.0, (0.0, 10.0))
            text = st.text_input("Enter text to overlay on the video", "My Holidays 2013")
            font_size = st.slider("Select text font size", 1, 100, 70)
            text_color = st.color_picker("Select text color", "#ffffff")
            text_position = st.selectbox("Select text position", ["center", "top", "bottom", "left", "right"])

        with col2:
            playback_speed = st.slider("Select video playback speed", 0.1, 3.0, 1.0, step=0.1)
            output_format = st.selectbox("Select output format", ["webm", "mp4"])

        if st.button("Edit Video"):
            with st.spinner("Processing..."):
                output_path = f"edited_video.{output_format}"
                success = edit_video(uploaded_file.name, output_path, start_time[0], start_time[1], text, font_size, text_color, playback_speed, output_format, text_position)

            if success:
                st.success(f"Video edited successfully. [Download Edited Video](./{output_path})")
                display_video(output_path, "Edited Video:")

if __name__ == "__main__":
    main()
