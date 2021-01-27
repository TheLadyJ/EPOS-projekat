import speech_recognition as sr


r=sr.Recognizer()

with sr.AudioFile('TheStory.wav') as source:
    r.adjust_for_ambient_noise(source)
    audio= r.record(source)
    try:
        print("Converting Audio File To Text...")
        text = r.recognize_google(audio)
        print("Converted Audio Is: \n" + text)
    except:
        print("sorry, could not recognise")