import speech_recognition as sr

import webbrowser as wb
r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('[search edureka: search youtube]')
    print('speak now')
    r3.adjust_for_ambient_noise(source, duration=1)
    audio = r3.listen(source, timeout=4)


if 'prva' in r1.recognize_google(audio):
    r1 = sr.Recognizer()

    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('search your query')
        r1.adjust_for_ambient_noise(source, duration=1)
        audio = r1.listen(source, timeout=4)
       
        try:
            get = r1.recognize_google(audio, language='sr-RS')
            print(get)
            wb.get().open_new_tab(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))
    

if 'druga' in r2.recognize_google(audio):
    r2 = sr.Recognizer()

    url = 'https://www.edureka.co/'
    with sr.Microphone() as source:
        print('search your query')
        r2.adjust_for_ambient_noise(source, duration=1)
        audio = r2.listen(source, timeout=4)
       
        try:
            get = r2.recognize_google(audio, language='sr-RS')
            print(get)
            wb.get().open_new_tab(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))
