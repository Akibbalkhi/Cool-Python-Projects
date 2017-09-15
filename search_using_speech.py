#Modules required are speech_recognition and google.They can be installed using
#pip3 install SpeechRecognition 
#pip3 install google
#Also requires beautifulsoup4


import speech_recognition as sr
from google import search
r = sr.Recognizer()
r.energy_threshold = 3500


with sr.Microphone() as source:  
    r.adjust_for_ambient_noise(source)
    print("Speak what do you want to search!")  
    audio = r.listen(source)
    print("Done listening!")
try:
    query= r.recognize_google(audio)
    for j in search(query,tld="co.in",num=10,stop=1,pause=2):
        print(j+"-"+query)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


