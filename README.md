# Jarvis AI Assistant
A voice controlled AI assistant built with Python that combines speech recognition, text-to-speech, and Google's Gemini AI to create a personalized virtual assistant experience.

# ✨ Features:

🎤 `Voice Recognition`: Wake word detection with "Jarvis"<br>
🗣️ `Text-to-Speech`: Natural voice responses using Google TTS<br>
🧠 `AI Integration`: Powered by Google Gemini for intelligent responses<br>
🌐 `Web Navigation`: Quick access to popular websites<br>
🎵 `Music Playback`: Voice controlled music from your library<br>
📰 `News Updates`: Fetch latest headlines from News API<br>
⚡ `Fast Commands`: Optimized hardcoded commands for common tasks<br>

# 🛠️ Installation:
**Prerequisites:**

  1. Python 3.7 or higher<br>
  2. Requires a microphone for voice input<br>
  3. API keys must be valid for features to work<br>
  4. Requires an internet connection for gTTS, NewsAPI, and Gemini AI<br>

# Required Dependencies:

pip install `speechrecognition`<br>
pip install `pyttsx3`<br>
pip install `requests`<br>
pip install `google-generativeai`<br>
pip install `gtts`<br>
pip install `pygame`<br>
pip install `pyaudio`<br>

# API Keys Setup:

  • News API: Get your free API key from NewsAPI.<br>
  • Google Gemini API: Get your API key from Google AI Studio.

# 📁 Project Structure:

jarvis-ai-assistant/<br>
├── main.py           # Main assistant code<br>
├── musicLibrary.py   # Predefined song names & YouTube links<br>
└── README.md         # Project documentation

# ⚙️ Configuration:

Before running the assistant, update the API keys in `main.py`:

  • NEWS_API_KEY = "Your-API"<br>
  • GEMINI_API_KEY = "Your-API"

# 🚀 Usage:
**Run the assistant:**

python `main.py`

  1. Wait for "Initializing Jarvis..." message
  2. Say "Jarvis" to wake the assistant
  3. Wait for "Yes, Sameer" response
  4. Give your command within 6 seconds

# 📋 Function Documentation:
**Core Functions:**

`speak(text)`

**Purpose:** Converts text to speech using Google's TTS engine.

**How it works:**

  1. Creates a gTTS (Google Text-to-Speech) object
  2. Saves audio to temporary MP3 file
  3. Uses pygame to play the audio
  4. Automatically cleans up temporary files
  5. Falls back to error handling if TTS fails

**Parameters:**

  • `text` (string): Text to be spoken

`speak_old(text)`

**Purpose:** Alternative text-to-speech using offline pyttsx3 engine.

**How it works:**

  • Uses the local pyttsx3 engine for offline TTS<br>
  • More reliable but less natural sounding than Google TTS

**Parameters:**

  • `text` (string): Text to be spoken

`aiProcess(command)`

**Purpose:** Processes natural language commands using Google Gemini AI.

**How it works:**

  1. Sends user command to Gemini 1.5 Flash model
  2. Uses system instruction to maintain Jarvis personality
  3. Returns AI generated response text
  4. Includes error handling for API failures

**Parameters:**

  1. `command` (string): User's voice command

**Returns:** AI generated response text

`processCommand(c)`

**Purpose:** Main command processor that handles both hardcoded and AI commands.

# How it works:

**1. Website Navigation (Hardcoded for speed)**:

  • "open google" → Opens Google<br>
  • "open chatgpt" → Opens ChatGPT<br>
  • "open github" → Opens developer's GitHub profile<br>
  • "open linkedin" → Opens developer's LinkedIn profile


**4. Music Playback:**

  • Command format: "play [song_name]"<br>
  • Searches musicLibrary.py for song links<br>
  • Opens YouTube links in default browser<br>
  • Provides feedback if song not found


**3. News Updates:**

  • Triggers on "news" keyword<br>
  • Fetches top US headlines from News API<br>
  • Reads first 3 headlines aloud<br>
  • Handles API errors gracefully


**5. AI Fallback:**

  • Any unrecognized command goes to Gemini AI<br>
  • Provides intelligent responses for general queries<br>

**Parameters:**

  • `c` (string): Voice command from user

# 🎵 Music Library:

The `musicLibrary.py` file contains a dictionary of song names mapped to YouTube URLs:

music = {<br>
    "stealth": "YouTube URL",<br>
    "march": "YouTube URL",<br>
    "skyfall": "YouTube URL",<br>
    "wolf": "YouTube URL"<br>
}

**Usage:** Say "play [song_name]" where song_name matches a key in the dictionary.<br>
**Adding Songs:** Add new entries to the music dictionary in the format `"song_name": "youtube_url"`

# Modifying Voice Settings:

Adjust recognition parameters in the main loop:

  • `timeout`: Maximum wait time for voice input<br>
  • `phrase_time_limit`: Maximum length of spoken phrase<br>
  • `duration`: Ambient noise adjustment time

# Changing AI Personality:

Modify the system instruction in the Gemini model configuration:

`system_instruction="Your custom personality instructions here"`

# 📄 License:

This project is open source and available under the MIT License.

# 🤝 Contributing:

Feel free to fork this project and submit pull requests for improvements!

# 👨‍💻 Developer:

**Sameer Ahmed Qureshi**

`Portfolio`: https://sameer-personall-portfolio.vercel.app <br>
`LinkedIn`: https://www.linkedin.com/in/sameer-ahmed-qureshi56

<hr>

Built with using Python and Google AI
