from flask import Flask, request, jsonify
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
import os

app = Flask(__name__)

# Model ve işlemci yükleme
processor = Wav2Vec2Processor.from_pretrained("mpoyraz/wav2vec2-xls-r-300m-cv8-turkish")
model = Wav2Vec2ForCTC.from_pretrained("mpoyraz/wav2vec2-xls-r-300m-cv8-turkish")

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        waveform, sample_rate = torchaudio.load(file)
        resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
        waveform = resampler(waveform)
        input_values = processor(waveform.squeeze().numpy(), return_tensors="pt", sampling_rate=16000).input_values

        with torch.no_grad():
            logits = model(input_values).logits
            predicted_ids = torch.argmax(logits, dim=-1)

        transcription = processor.batch_decode(predicted_ids)
        return jsonify({'transcription': transcription[0]})

if __name__ == '__main__':
    app.run(debug=True)

