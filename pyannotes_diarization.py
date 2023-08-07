#!pip install   pyannote.audio
from pyannote.audio import Pipeline


pipeline = Pipeline.from_pretrained('pyannote/speaker-diarization', use_auth_token="hf token")

DEMO_FILE = {'uri': 'blabal', 'audio': 'audio.wav'}
dz = pipeline(DEMO_FILE)  

with open("diarization.txt", "w") as text_file:
    text_file.write(str(dz))
print(*list(dz.itertracks(yield_label = True))[:10], sep="\n")

def millisec(timeStr):
  spl = timeStr.split(":")
  s = (int)((int(spl[0]) * 60 * 60 + int(spl[1]) * 60 + float(spl[2]) )* 1000)
  return s

import re
dz = open('diarization.txt').read().splitlines()
dzList = []
for l in dz:
  start, end =  tuple(re.findall('[0-9]+:[0-9]+:[0-9]+\.[0-9]+', string=l))
  start = millisec(start) - 2000 
  end = millisec(end)  - 2000 
  lex = not re.findall('SPEAKER_01', string=l)
  dzList.append([start, end, lex])

print(*dzList[:10], sep='\n')
