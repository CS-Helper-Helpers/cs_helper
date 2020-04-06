from gtts import gTTS  # google text to speech
import playsound  # to play saved mp3 file
import os  # to save/open files


class TTS():
    """
    Text to Speech
    """

    def __init__(self):
        self.output = None

    def _set_output(self, output):
        self.output = output

    def assistant_speaks(self, output):
        self._set_output(output)

        # Create gTTS instance
        toSpeak = gTTS(text=self.output, lang='en', slow=False)

        # Save the audio file given by Google Text to Speech
        file = "speak.mp3"
        toSpeak.save(file)

        # Playsound package is used to play the same file.
        playsound.playsound(file, True)
        os.remove(file)

