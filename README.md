🗣️ Speech-to-Text Converter using Python

This is a Python-based Speech-to-Text converter that captures audio input from your microphone and converts it into text using Google's Speech Recognition API. It's built using the speech_recognition and pyaudio libraries.

🛠️ Features
Captures live voice input from your system's microphone

Converts speech to text using Google's free speech recognition service

Provides real-time feedback on what was said

Handles errors like unclear audio or network issues

💡 How It Works
Initializes the recognizer with speech_recognition.Recognizer().

Uses your default microphone to capture audio input.

Sends the audio to Google’s Speech Recognition API.

Displays the recognized text on the screen.

Handles common errors such as:

Unclear or inaudible audio

Network issues during API request

✅ Example Output

Please speak something...
Converting speech to text...
You said: Hello, this is a test
If audio is unclear:
Sorry, could not understand the audio.

If there’s a request failure:
Could not request results from Google Speech Recognition service.

🧰 Requirements
Python 3.x

speechrecognition

pyaudio (for microphone input)

Installation
You can install the dependencies with:


pip install SpeechRecognition
pip install PyAudio

🔒 Limitations
Requires an active internet connection for Google API.

Speech recognition accuracy may vary based on microphone quality and background noise.

