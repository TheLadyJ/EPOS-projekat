import speech_recognition as sr


r=sr.Recognizer()

with sr.AudioFile('Krishnamurti.wav') as source:
    r.adjust_for_ambient_noise(source)
    audio= r.listen(source)
    try:
        print("Converting Audio File To Text...")
        text = r.recognize_google(audio)
        print("Converted Audio Is: \n" + text)
    except:
        print("sorry, could not recognise")