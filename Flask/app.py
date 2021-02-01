from pytube import YouTube
from moviepy.editor import *
import os, shutil
from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    transcript=""
    if request.method == "POST":
        print("Form data received")

        url=""

        url = request.form["url"]
        

        if url:
            try:
                mp4 = YouTube(url).streams.get_highest_resolution().download()
                mp3 = mp4.split(".mp4",1)[0] + ".wav"

                video_clip = VideoFileClip(mp4)
                audio_clip = video_clip.audio
                audio_clip.write_audiofile(mp3)

                audio_clip.close()
                video_clip.close()

                os.remove(mp4)

                recognizer = sr.Recognizer()

                with sr.AudioFile(mp3) as source:
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.record(source)
                    try:
                        print("Converting Audio File To Text...")
                        transcript = recognizer.recognize_google(audio)
                    except:
                        transcript = "Sorry, transcription failed."
                os.remove(mp3)

            except:
                transcript = "Sorry, no video found."

            

    return render_template('index.html', transcript=transcript)

if __name__=="__main__":
    app.run(debug=True, threaded=True)

