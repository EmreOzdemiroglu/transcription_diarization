# Cutting the video
# pip install pydub
from pydub import AudioSegment

t1 = 0 * 1000 #Works in milliseconds
t2 = 20 * 60 * 1000

newAudio = AudioSegment.from_wav("voice.wav")
a = newAudio[t1:t2]
a.export("audio1.wav", format="wav")

# pyannote.audio seems to miss the first 0.5 seconds of the audio, therefore we prepend a spcacer.

audio = AudioSegment.from_wav("audio1.wav")
spacermilli = 2000
spacer = AudioSegment.silent(duration=spacermilli)
audio = spacer.append(audio, crossfade=0)

audio.export('audio.wav', format='wav')




