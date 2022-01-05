import streamlit as st
from PIL import Image
import pytesseract
from googletrans import Translator
from gtts import gTTS
import playsound
from time import sleep
import os
import pyglet

def audio(text, lang):
    tts = gTTS(text = text, lang = lang, slow = True)
    filename = "audio.mp3"
    tts.save(filename)
    music = pyglet.media.load(filename, streaming = False) #loading audio file
    #'streaming': True if the source should be streamed from disk,
    #False if it should be entirely decoded immediately
    
    music.play() #to play it immediately 
    sleep(music.duration) #wait till audio length
    os.remove(filename) #remove the saved file
    

def main():    
    st.title("Fun with image") #Title    
    file = st.file_uploader("Upload an image") #For uploading Image 
    submit = st.button("Extract Text")

    if file and submit:        
        image = Image.open(file) #opening the image               
        pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract\tesseract.exe" #providing the tesseract executable location to pytesseract library
        text = pytesseract.image_to_string(image) #this function will extract the text from the image
        st.image(image, caption='Live photo') #Load full image
        st.write(text) #printing text extracted from image
    
    txt = st.text_input("Enter text to translate") #input text for translation
    option = st.selectbox('Pick a language',('Arabic',
                                             'Bengali',
                                             'English',
                                             'French',
                                             'Gujarati',
                                             'Hindi',
                                             'Japanese',                                             
                                             'Russian',
                                             'Spanish',
                                             'Telugu',
                                             'Urdu',)) #select any language from dropdown menu

    if option:
        st.write('You selected:', option) #print selected language
        
    lang = 'en' #default translation language
    if option == 'Arabic':
        lang = 'ar'
    elif option == 'Bengali':
        lang = 'bn'
    elif option == 'English':
        lang = 'en'
    elif option == 'French':
        lang = 'fr'
    elif option == 'Gujarati':
        lang = 'gu'
    elif option == 'Hindi':
        lang = 'hi'
    elif option == 'Japanese':
        lang = 'ja'
    elif option == 'Russian':
        lang = 'ru'
    elif option == 'Spanish':
        lang = 'es'
    elif option == 'Telugu':
        lang = 'te'
    elif option == 'Urdu':
        lang = 'ur'
                
    speak = st.button("Speak")

    if len(txt) > 0:
        translator = Translator()
        result = translator.translate(txt, dest=lang) #translating to selected language
        st.write("PRONUNCIATION:",result.pronunciation)
        st.write("TRANSLATION:",result.text) #printing translated text        
        if speak:
            audio(result.text,lang) #function to convert text to speech  

if __name__=="__main__":
    main()        
    

