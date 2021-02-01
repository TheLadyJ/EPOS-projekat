from pytube import YouTube
from moviepy.editor import *
import os, shutil
import speech_recognition as sr

def get_mp3():
    url=input("Enter a Youtube link:")
    output="wav"
    print("Converting...")

    mp4 = YouTube(url).streams.get_highest_resolution().download()
    mp3 = mp4.split(".mp4",1)[0] + f".{output}"

    video_clip = VideoFileClip(mp4)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3)

    audio_clip.close()
    video_clip.close()

    os.remove(mp4)
    r=sr.Recognizer()
    with sr.AudioFile(mp3) as source:
        r.adjust_for_ambient_noise(source)
        audio= r.record(source)
        try:
         print("Converting Audio File To Text...")
         text = r.recognize_google(audio)
         print("Converted Audio Is: \n" + text)
        except:
            print("sorry, could not recognise")
    os.remove(mp3)
get_mp3()