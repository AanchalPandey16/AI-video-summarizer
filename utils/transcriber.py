import whisper
import os


def get_next_filename():

    os.makedirs("scrap", exist_ok=True)

    files = os.listdir("scrap")

    numbers = []

    for file in files:
        name = file.split(".")[0]
        if name.isdigit():
            numbers.append(int(name))

    next_number = max(numbers, default=0) + 1

    return f"scrap/{next_number}.txt"


def transcribe_audio(audio_file, model_name):

    if not os.path.exists(audio_file):
        raise FileNotFoundError(f"Audio file not found: {audio_file}")

    model = whisper.load_model(model_name)

    result = model.transcribe(audio_file)

    file_path = get_next_filename()

    with open(file_path, "w", encoding="utf-8") as f:

        f.write(f"Detected Language: {result['language']}\n\n")

        for segment in result["segments"]:
            start = round(segment["start"], 2)
            end = round(segment["end"], 2)
            text = segment["text"]

            f.write(f"[{start} - {end}] {text}\n")

    return result["text"]