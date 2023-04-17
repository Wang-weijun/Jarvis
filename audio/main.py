import speech_recognition as sr

# 在Recognizer中可以接入不同公司的语音识别API
r = sr.Recognizer()

harvard = sr.AudioFile('data\harvard.wav')
with harvard as source:
    audio = r.record(source)
print(r.recognize_google(audio, language='zh-CN'))
