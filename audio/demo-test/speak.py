from gtts import gTTS
import pyttsx3

# engine = pyttsx3.init()
# engine.say('I will speak this text')
# engine.say('你好')
# engine.runAndWait()

# 保存音频
# china = '你好，我是贾维斯'
# obj = gTTS(text = china, slow = False, lang='zh-CN')
# obj.save('chinese.mp3')

english = 'hi jarvis'
obj = gTTS(text = english, slow = False, lang='es-us')
obj.save('english.mp3')