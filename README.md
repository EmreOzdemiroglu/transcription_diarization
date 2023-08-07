# Türkçe Ses Transkripsiyonu Flask API

## Kurulum

1. **Gerekli Kütüphanelerin Kurulumu**: Proje, `requirements.txt` dosyasında belirtilen Python kütüphanelerini kullanmaktadır. Bu kütüphaneleri aşağıdaki komutla yükleyebilirsiniz:

   ```bash
   pip install -r requirements.txt
   ```
2. Kenlm kurulumu. Ben arch kullandığımdan kurulum için internete baktım. Hata ayıklama yaparken gerekliydi bende yükledim. *not*

## Kullanım

1. **API'yi Başlatma**: Terminalde, projenin ana dizininde aşağıdaki komutu çalıştırın:

   ```bash
   python app.py
   ```

   Bu, API'yi `http://127.0.0.1:5000/` adresinde başlatacaktır.

2. **Transkripsiyon İsteği Gönderme**: Ses dosyasının transkripsiyonunu almak için, aşağıdaki `curl` komutunu kullanabilirsiniz:

   ```bash
   curl -X POST -F "files=@dosya_yolu1.mp3" -F "files=@dosya_yolu2.mp3" http://localhost:5000/transcribe
   ```

   Bu komut, `voice.mp3` adlı dosyayı API'ye gönderir ve transkripsiyon sonucunu JSON olarak döndürür.


## Lisans

MIT License

Copyright (c) [2023] [EmreOzdemiroglu]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

