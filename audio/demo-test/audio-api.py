import speech_recognition as sr

# 在Recognizer中可以接入不同公司的语音识别API
r = sr.Recognizer()
mir = sr.Microphone()
with mir as source:
    # 处理噪音
    # r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
languages = ['zh-CN', 'en-US', 'ja-JP']
try:
    print(r.recognize_google(audio, language='en-US'))
except sr.UnknownValueError:
    print('不能理解当前语音')
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
