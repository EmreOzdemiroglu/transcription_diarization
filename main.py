import subprocess
import whisper
import datetime
import torch
import pyannote.audio
from pyannote.audio.pipelines.speaker_verification import PretrainedSpeakerEmbedding
from pyannote.audio import Audio
from pyannote.core import Segment
import wave
import contextlib
from sklearn.cluster import AgglomerativeClustering
import numpy as np


def convert_to_wav(file_path):
    """Convert file to WAV format if not already in that format."""
    if file_path[-3:] != 'wav':
        subprocess.call(['ffmpeg', '-i', file_path, 'audio.wav', '-y'])
        return 'audio.wav'
    return file_path

def load_embedding_model():
    """Load the speaker embedding model."""
    return PretrainedSpeakerEmbedding(
        "speechbrain/spkrec-ecapa-voxceleb",
        device=torch.device("cuda")
    )

def get_file_duration(file_path):
    """Return the duration of the audio file."""
    with contextlib.closing(wave.open(file_path, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    return duration

def segment_embedding(audio_path, segment, duration, embedding_model):
    """Get the embedding for a given audio segment."""
    start = segment["start"]
    end = min(duration, segment["end"])
    clip = Segment(start, end)
    waveform, _ = Audio().crop(audio_path, clip)
    return embedding_model(waveform[None])

def get_embeddings(audio_path, segments, duration, embedding_model):
    """Generate embeddings for each segment."""
    embeddings = np.zeros(shape=(len(segments), 192))
    for i, segment in enumerate(segments):
        embeddings[i] = segment_embedding(audio_path, segment, duration, embedding_model)
    return np.nan_to_num(embeddings)

def write_transcript(segments):
    """Write the transcript to a file."""
    with open("transcript.txt", "w") as f:
        for (i, segment) in enumerate(segments):
            if i == 0 or segments[i - 1]["speaker"] != segment["speaker"]:
                f.write("\n" + segment["speaker"] + ' ' + str(datetime.timedelta(seconds=round(segment["start"]))) + '\n')
            f.write(segment["text"][1:] + ' ')

def transcribe_audio(path: str):
    """
    Transcribe the audio file and return the transcript.
    
    Args:
    - path (str): Path to the audio file.
    
    Returns:
    - str: Path to the transcript file.
    """
    # Convert the audio file to WAV format if required
    path = convert_to_wav(path)
    
    # Load the Whisper model and transcribe the audio
    model = whisper.load_model('medium')
    result = model.transcribe(path)
    segments = result["segments"]
    
    # Get the duration of the audio file and load the embedding model
    duration = get_file_duration(path)
    embedding_model = load_embedding_model()
    embeddings = get_embeddings(path, segments, duration, embedding_model)
    
    # Perform clustering to identify speakers
    clustering = AgglomerativeClustering(2).fit(embeddings)
    labels = clustering.labels_
    for i in range(len(segments)):
        segments[i]["speaker"] = 'SPEAKER ' + str(labels[i] + 1)
    
    # Write the transcript to a file
    transcript_file = path.rsplit('.', 1)[0] + '_transcription.txt'
    with open(transcript_file, "w") as f:
        for (i, segment) in enumerate(segments):
            if i == 0 or segments[i - 1]["speaker"] != segment["speaker"]:
                f.write("\n" + segment["speaker"] + ' ' + str(datetime.timedelta(seconds=round(segment["start"]))) + '\n')
            f.write(segment["text"][1:] + ' ')
    
    return transcript_file


