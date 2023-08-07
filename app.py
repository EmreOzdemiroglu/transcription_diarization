
from flask import Flask, request, jsonify
import os

# Importing necessary functions from main1.py
from main import transcribe_audio

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    # Check if files are present in the request
    if 'files' not in request.files:
        return jsonify({'error': 'No files provided.'}), 400

    files = request.files.getlist('files')
    output_files = []
    for file in files:
        filename = os.path.join("./", file.filename)
        file.save(filename)
        transcript_file = transcribe_audio(filename)
        output_files.append(transcript_file)

    return jsonify({'transcribed_files': output_files})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
