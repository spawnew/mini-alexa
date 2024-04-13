import speech_recognition as sr # type: ignore
import webbrowser
import pyttsx3 # type: ignore
#webbrowzer para abrir el explorarodr 
#speech_recognition para el reconocimiento de voz
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def talk():
    mic = sr.Microphone()
    with mic as source:
        audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio, language='es-AR')
    print(f'Has dicho: {text}')
    return text.lower()

 
while True :
    text = talk()
    
    if 'comprar' in text:
       engine.say('¿Qué quieres comprar en MercadoLibre?')
       engine.runAndWait()
       text = talk()
       webbrowser.open(f'https://www.mercadolibre.com.ar/#from={text}') 
    if 'nada' in text:
      engine.say('porque me molestas entonces')
      engine.runAndWait()
      text = talk()
    if 'hola' in text:
       engine.say('Hola como estas lucas que deseas hacer ')
       engine.runAndWait()
       text = talk()