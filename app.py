import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # Load all the environment variables
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e

def generate_gemini_content(transcript_text, prompt, length):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt.format(length=length) + transcript_text)
    return response.text

st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

length = st.number_input("Enter the desired summary length:", min_value=50, max_value=500, step=10, value=250)

if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        prompt = """You are Yotube video summarizer. You will be taking the transcript text
        and summarizing the entire video and providing the important summary in points
        within {length} words. Please provide the summary of the text given here:  """
        summary = generate_gemini_content(transcript_text, prompt, length)
        st.markdown("## Detailed Notes:")
        st.write(summary)
