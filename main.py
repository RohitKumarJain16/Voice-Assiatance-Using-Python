import speech_recognition as sr
import webbrowser
import pyttsx3
import music_Libaray
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "ae06f0e20d31461c89c5a5f2ad20c604"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        speak("Ya sure, Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Ya sure, Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower():
        speak("Ya sure, Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif c.lower().startswith("play"):
        # Fixing the "play" command parsing
        song = c.lower().split("play", 1)[1].strip()
        if song in music_Libaray.music:
            link = music_Libaray.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}")

    elif "News" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=API Key")
        if r.status_code==200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles:
                speak(article['title'])
                

if __name__ == "__main__":
    speak("Hi Shubh, I am Tank ready for boom!")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Adjust once before the loop

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for the wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            wake_word = recognizer.recognize_google(audio).lower()
            print(f"Heard: {wake_word}")

            if wake_word == "Tank":
                speak("Tank here!")
                with sr.Microphone() as source:
                    print("Listening for your command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                command = recognizer.recognize_google(audio)
                print(f"Command: {command}")
                processCommand(command)
            else:
                print("Wake word not detected. Waiting...")

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error: {e}")