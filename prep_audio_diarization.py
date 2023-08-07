from pydub import AudioSegment
import re 


audio = AudioSegment.from_wav("audio.wav")
spacermilli = 2000
spacer = AudioSegment.silent(duration=spacermilli)

sounds = spacer
segments = []


def millisec(timeStr):
  spl = timeStr.split(":")
  s = (int)((int(spl[0]) * 60 * 60 + int(spl[1]) * 60 + float(spl[2]) )* 1000)
  return s

dz = open('diarization.txt').read().splitlines()
for l in dz:
  start, end =  tuple(re.findall('[0-9]+:[0-9]+:[0-9]+\.[0-9]+', string=l))
  start = int(millisec(start)) #milliseconds
  end = int(millisec(end))  #milliseconds
  
  segments.append(len(sounds))
  sounds = sounds.append(audio[start:end], crossfade=0)
  sounds = sounds.append(spacer, crossfade=0)

sounds.export("dz.wav", format="wav") #Exports to a wav file in the current path.

print(segments[:8])
