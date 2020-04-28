from gtts import gTTS            # gTTS = Google Text To speech


def text_To_Speech(file):
    language = "en"                                            # It specifies which language has to be chosen
    audio = gTTS(text=file, lang=language, slow=False)         # It will convert the text into Speech...
    audio.save("speak.wav")                                    # It will save the audio file.....


if __name__ == '__main__':
    file = open("text.txt")                                    # To open the File containing the required Text..
    x = file.read()                                            # To read the text containing in the file

    text_To_Speech(x)
