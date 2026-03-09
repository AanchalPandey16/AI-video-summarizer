from utils.video_downloader import download_audio
from utils.transcriber import transcribe_audio
from utils.summary import summarize_text

url = input("Enter video URL: ")

audio = download_audio(url)
transcript = transcribe_audio(audio)
summary = summarize_text(transcript)

print("Transcript saved")