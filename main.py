import speech_recognition as sr
import pyaudio

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use your microphone to capture input
with sr.Microphone() as source:
    print("Please speak something...")
    audio = recognizer.listen(source)

    try:
        print("Converting speech to text...")
        text = recognizer.recognize_google(audio)
        print("You said: ", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
