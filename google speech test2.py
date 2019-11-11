from gtts import gTTS
import os
file = input("Read from file: ")
contents = open(file)
say = contents.read()
print("\nGenerating speech. Be patient. This could take a while...\n")
tts = gTTS(text=say, lang='en')
tts.save("text.mp3")
os.system("killall mpv")
os.system("mpv text.mp3")
os.remove("text.mp3")
