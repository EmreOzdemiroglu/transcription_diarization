from flask import Flask, request, Response
from transformers import pipeline
import torchaudio
import json

app = Flask(__name__)

# Modeli yükleme
pipe = pipeline("automatic-speech-recognition", model="emre/whisper-medium-turkish-2")

@app.route('/transcribe', methods=['POST'])
def transcribe():
    file = request.files['file']
    file.save('temp_voice.mp3')

    # Ses dosyasını okuma
    waveform, sample_rate = torchaudio.load('temp_voice.mp3')

    # Örnekleme oranını 16000'e dönüştürme
    resampler = torchaudio.transforms.Resample(sample_rate, 16000)
    waveform_16k = resampler(waveform)

    # 16k örnekleme oranıyla geçici dosya oluşturma
    torchaudio.save('temp_voice_16k.mp3', waveform_16k, 16000)

    # Ses dosyasını işleme
    transcription = pipe('temp_voice_16k.mp3')
    
    # Düzgün şekilde JSON yanıtı döndürme
    response_data = {'transcription': transcription['text']}
    return Response(json.dumps(response_data, ensure_ascii=False), content_type='application/json; charset=utf-8')

if __name__ == '__main__':
    app.run(debug=True)

