import streamlit as st
from utils.video_downloader import download_audio
from utils.transcriber import transcribe_audio
from utils.summary import summarize_text

st.title("AI Video Summarizer")

url = st.text_input("Enter YouTube URL")

model_option = st.selectbox(
    "Choose transcription quality",
    [
        "tiny (fast)",
        "base",
        "medium (better accuracy)",
        "large (best accuracy)"
    ]
)

if st.button("Generate Summary"):

    try:

        st.write("Downloading audio...")
        audio = download_audio(url)
        st.success(f"Audio saved at {audio}")

        model_name = model_option.split()[0]

        st.write("Transcribing audio...")
        transcript = transcribe_audio(audio, model_name)
        st.success("Transcript saved in scrap folder")

        st.write("Generating summary...")
        summary = summarize_text(transcript)
        st.success("Summary saved in summary folder")

        st.subheader("Summary")
        st.write(summary)

    except Exception as e:
        st.error(f"Error: {e}")