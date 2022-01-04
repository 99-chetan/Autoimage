import streamlit as st
from PIL import Image
import pytesseract
from googletrans import Translator
import pyttsx3
from gtts import gTTS
import playsound
from tempfile import TemporaryFile
from time import sleep
import os
import pyglet

def sp(text,lang):
    tts=gTTS(text=text, lang=lang,slow=True)
    filename="audio.mp3"
    tts.save(filename)
    #playsound.playsound(filename)
    music = pyglet.media.load(filename, streaming=False)
    music.play()
    sleep(music.duration) #prevent from killing
    os.remove(filename) 



def main():
    st.title("Fun with image")
    file=st.file_uploader("Upload an image")
    submit = st.button("Extract Text")
    #if submit:
        #st.write("Done!!")
        #slide=st.sidebar.write("""# Surprise""")

    if file and submit:
        image = Image.open(file)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract\tesseract.exe"
        text = pytesseract.image_to_string(image)
        st.image(image, caption='Live photo')
        st.write(text)
    
    txt=st.text_input("Enter text to translate")
    option=st.selectbox('Pick a language',('English','French','Gujarati','Hindi','Russian','Urdu'))
    if option:
        st.write('You selected:', option)
    lang='en'
    if option=='English':
        lang='en'
    elif option=='French':
        lang='fr'
    elif option=='Gujarati':
        lang='gu'
    elif option=='Russian':
        lang='ru'
    elif option=='Urdu':
        lang='ur'
    elif option=='Hindi':
        lang='hi'
    
    speak = st.button("Speak")

    if len(txt)>0:
        translator = Translator()
        result = translator.translate(txt, src='en', dest=lang)
        st.write(result.text)
        #if speak:
            #engine = pyttsx3.init()
            #engine.say(result.text)
            #engine.runAndWait()  
        if speak:
            sp(result.text,lang)

if __name__=="__main__":
    main()        
    

