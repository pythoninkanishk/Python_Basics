import speech_recognition as sr
import webbrowser
import pyttsx3
import MusicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "d74e1f34e23a4f558fef0ee4ee278cc2"  # your API key


def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        articles = data["articles"][:5]  # top 5 headlines
        news_list = []
        for article in articles:
            news_list.append(article["title"])
        return news_list
    else:
        return ["Sorry, I could not fetch the news right now."]


def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        try:
            song = c.lower().split(" ")[1]
            Link = MusicLibrary.music.get(song, None)
            if Link:
                speak(f"Playing {song}")
                webbrowser.open(Link)
            else:
                speak("Sorry, I couldn't find that song.")
        except IndexError:
            speak("Please tell me which song to play.")
    elif "news" in c.lower():
        speak("Fetching the latest news...")
        headlines = get_news()
        speak("Here are the top headlines")
        for idx, headline in enumerate(headlines, 1):
            print(f"{idx}. {headline}")
            speak(headline)
    else:
        speak("Sorry, I didn't understand that command.")


if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes, how can I help you?")
                with sr.Microphone() as source:
                    print("Jarvis activated, listening for command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
                    command = recognizer.recognize_google(audio)
                    print("You said:", command)
                    processCommand(command)

        except sr.UnknownValueError:
            # speech not clear
            pass
        except sr.RequestError:
            print("Speech recognition service unavailable.")
        except Exception as e:
            print("Error:", e)
