import sys
import ctypes
import speech_recognition as sr

voice = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    # listen but avoid background noise
    voice.adjust_for_ambient_noise(source)
    # listen for 5 seconds
    audio = voice.listen(source, timeout=5)

try:
    what_you_said = voice.recognize_google(audio)
    print("You said: " + what_you_said)
    if what_you_said == "stop":
        print("Stopping...")
        sys.exit()
    elif what_you_said == "lock my PC":
        print("Locking...")
        ctypes.windll.user32.LockWorkStation()
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))