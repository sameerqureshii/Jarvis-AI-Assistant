import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai
from gtts import gTTS
import pygame
import os

# API Key Configuration
# IMPORTANT: Replace with your actual API keys
NEWS_API_KEY = "<Your-API>"
GEMINI_API_KEY = "<Your-API>" # Add your Gemini API key here

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash-latest', # A fast and capable model
    system_instruction="You are a virtual assistant named Jarvis skilled in general tasks. Please provide short, concise responses."
)
# End of Configuration

# Initialize other components
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# This function uses the older, offline text-to-speech engine
def speak_old(text):
    engine.say(text)
    engine.runAndWait()

# This function uses Google's Text-to-Speech for a more natural voice
def speak(text):
    if not text:
        print("Received empty text to speak.")
        return
    try:
        tts = gTTS(text)
        tts.save('temp.mp3')

        pygame.mixer.init()
        pygame.mixer.music.load('temp.mp3')
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
    except Exception as e:
        print(f"Error in speak function: {e}")
    finally:
        if pygame.mixer.get_init():
            pygame.mixer.music.unload()
        # Ensure the file is removed even if there was an error
        if os.path.exists("temp.mp3"):
            os.remove("temp.mp3")

# This function now calls the Gemini API
def aiProcess(command):
    """
    Sends a command to the Gemini model and returns the text response.
    """
    print(f"Sending to Gemini: '{command}'")
    try:
        response = model.generate_content(command)
        return response.text
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "Sorry, I couldn't process that request."

def processCommand(c):
    # Hard coded commands for speed and reliability
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com/sameerqureshii")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/in/sameer-ahmed-qureshi56")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song) # Use .get() for safety
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I don't have a link for the song {song}")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            speak("Here are the top headlines.")
            for article in articles[:3]: # Read top 3 headlines
                speak(article['title'])
        else:
            speak("Sorry, I couldn't fetch the news right now.")
    else:
        # If it's not a hard coded command, let Gemini handle it
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                word = recognizer.recognize_google(audio).lower().strip()
            
            if "jarvis" in word:
                speak("Yes, Sameer")
                with sr.Microphone() as source:
                    print("Jarvis Active... Listening for command.")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except sr.WaitTimeoutError:
            print("Listening timed out, waiting again...")
        except sr.UnknownValueError:
            # This is common, so we don't need to print anything
            pass

        except Exception as e:
            print(f"An unexpected error occurred: {e}")