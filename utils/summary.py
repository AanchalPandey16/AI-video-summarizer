import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_next_summary_filename():

    os.makedirs("summary", exist_ok=True)

    files = os.listdir("summary")

    numbers = []

    for file in files:
        name = file.split(".")[0]
        if name.isdigit():
            numbers.append(int(name))

    next_number = max(numbers, default=0) + 1

    return f"summary/{next_number}.txt"


def summarize_text(text):

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[
            {"role": "system",
             "content": """
             You are a transcription normalizer and summarizer.

The input may contain any type of spoken content: songs, shayari, educational videos, interviews, or general speech, in Hindi, Urdu, or mixed languages.

Your tasks:

Convert all text into clear English or Hinglish (Hindi written using English letters).

Never output Urdu or Hindi script; use only English alphabet characters.

Preserve the original meaning.

If the sentence is mostly Hindi/Urdu, convert it into Hinglish.

If it naturally translates well, convert it into simple English.

Keep the sentences clean, readable, and grammatically correct.

After conversion, create a concise summary in English or Hinglish explaining what the video/song/segment is about.

Include a timestamp for when the text was extracted.

Do not add explanations, commentary, or extra notes.
             
             """},
            {"role": "user", "content": text}
        ]
    )

    summary = response.choices[0].message.content

    file_path = get_next_summary_filename()

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(summary)

    return summary
