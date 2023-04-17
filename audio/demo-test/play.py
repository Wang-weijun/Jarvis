import tempfile
from gtts import gTTS
import speech_recognition
from pygame import mixer

mixer.init()


def listenTo():
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    return r.recognize_google(audio, language='zh-CN')


def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts =gTTS(text = sentence, lang='zh-CN')
        tts.save('{}.mp3'.format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()


# speak('大家好！祝大家有个美好的一天')
# 重复所听到的语音
speak(listenTo())

# 根据下面回复
# Answer = {
#     '你好吗': '我很好',
#     '你很帅': '谢谢啦',
#     '再见了': '下次再见！拜拜'
# }
# speak(Answer.get(listenTo(), '对不起，请再说一次！'))
