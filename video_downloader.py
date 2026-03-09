import yt_dlp
import os


def download_audio(video_url):

    os.makedirs("video", exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "video/%(title)s.%(ext)s",
        "restrictfilenames": True,

        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(video_url, download=True)

        base_file = ydl.prepare_filename(info)

        audio_path = os.path.splitext(base_file)[0] + ".mp3"

    return audio_path