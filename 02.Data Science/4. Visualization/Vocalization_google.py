from gtts import gTTS

default_str="""
안녕하세요 """

emotion_str="안녕하세요. 안녕하세요! 안녕하세요? 안녕하세요.. 젠장. 젠장? 젠장!"

def speaker(a):
    tts=gTTS(text=a, lang='ko')
    tts.save('test.mp3')

    open('test.mp3')
speaker(emotion_str)