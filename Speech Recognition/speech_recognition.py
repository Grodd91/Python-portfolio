import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    audio = recognizer.listen(source)

try:
    recognized_text = recognizer.recognize_google(audio, language="en-US")
    print(recognized_text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print(f"Error from the server: {e}")
