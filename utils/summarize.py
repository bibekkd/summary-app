import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def get_api_key():
    try:
        return st.secrets["API_KEY"]
    except KeyError:
        api_key = os.getenv('GEMINI_API_KEY')
        if api_key:
            return api_key
        else:
            st.error("No API key found. Please set the API key in .streamlit/secrets.toml or as an environment variable 'GEMINI_API_KEY'")
            st.stop()


api_key = get_api_key()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_summary(text, length):
    length_map = {
        "Short": "Provide a concise summary of the following text.",
        "Medium": "Provide a detailed summary of the following text.",
        "Long": "Provide an in-depth summary of the following text.",
    }

    prompt = f"""
            Listen to me carefully: If you are given any text about any topic, 
            first analyze the full text thoroughly. 
            Identify the main theme, highlight the key points, 
            and capture only the essential information from the text.

            Follow the given example when generating a summary:

            Example:
            Original Text: 
            "AI agents are software programs that can autonomously 
            perform tasks and make decisions within a defined environment.
            They leverage artificial intelligence technologies 
            like machine learning and natural language processing to perceive their surroundings, 
            learn from experiences, and achieve specific goals. 2  Unlike traditional software, 
            which operates based on predefined rules, 
            AI agents can adapt and modify their behavior in response to changing conditions. 
            This adaptability makes them suitable for a wide range of applications, 
            including customer service, fraud detection, 
            and even complex scientific research."

            Summary Output :
            Here's the summary with highlights, main theme, and summary using essential information:

            Highlights:
                Autonomy: AI agents can perform tasks and make decisions independently.
                AI Technologies: Utilize machine learning and natural language processing.
                Adaptability: Can adjust behavior based on changing conditions.
                Versatility: Applicable across various domains like customer service, 
                fraud detection, and scientific research.

            Main Theme: 
                AI agents represent a significant advancement in software capabilities, 
                enabling autonomous and adaptive behavior driven by artificial intelligence technologies.

            Summary Using Essential Information: 
                AI agents are sophisticated software programs that leverage AI technologies 
                like machine learning and natural language processing. 
                They can operate independently, making decisions and 
                adapting to changing environments. This adaptability makes them valuable across 
                diverse applications, from customer service to scientific research.

            Now, based on the example provided above, generate summary using the same approach:

            Text:
            {text}
    """
    try:
        response = model.generate_content([prompt])
        return response.text  
    except Exception as e:
        return f"Error generating summary: {str(e)}"
