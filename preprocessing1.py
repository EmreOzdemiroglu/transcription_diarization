import librosa
import soundfile as sf
import noisereduce as nr
from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def preprocess_audio(input_file, output_file):
    # Dosyayı yükle
    audio, sr = librosa.load(input_file, sr=16000)

    # Gürültü azaltma
    noise_reduced_audio = nr.reduce_noise(y=audio, sr=sr)

    # İnsan sesi frekans aralığını vurgula
    voice_enhanced_audio = butter_bandpass_filter(noise_reduced_audio, 300, 3400, sr)

    # Sonucu kaydet
    sf.write(output_file, voice_enhanced_audio, sr)
    print(f"{output_file} dosyası başarıyla oluşturuldu.")

# Dosya adları
input_file = "voice.mp3" # Giriş dosyanızın adı
output_file = "processed_voice.wav" # İşlenmiş dosyanın adı

# Ön işleme işlemi
preprocess_audio(input_file, output_file)

