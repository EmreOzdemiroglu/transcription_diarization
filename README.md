# Türkçe Ses Transkripsiyonu Flask API

Bu proje, verilen bir ses dosyasının Türkçe transkripsiyonunu gerçekleştirmek üzere tasarlanmış bir Flask API'dir. [Hugging Face modeli](https://huggingface.co/mpoyraz/wav2vec2-xls-r-300m-cv8-turkish) kullanılarak ses dosyaları işlenir. Modelin eğitim ve değerlendirme verileri hakkında daha fazla bilgi için [bu bağlantıya](https://huggingface.co/mpoyraz/wav2vec2-xls-r-300m-cv8-turkish#training-and-evaluation-data) göz atabilirsiniz.

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
   curl -X POST -F "file=@voice.mp3" http://127.0.0.1:5000/transcribe
   ```

   Bu komut, `voice.mp3` adlı dosyayı API'ye gönderir ve transkripsiyon sonucunu JSON olarak döndürür.

## Gelecek Geliştirmeleri
- [ ] OpenAI API ile Bağlam Düzeltme: Transkripsiyon sürecinde ortaya çıkan dilbilgisel ve anlamsal hataları düzeltmek için OpenAI'nin güçlü dil modelini entegre etmek. Bu, cümlenin bağlamına göre kelime seçimlerini optimize edebilir ve transkripsiyonun genel kalitesini artırabilir. Bu özellik, özellikle karmaşık ve teknik terimler içeren ses dosyaları için yararlı olabilir.

- [ ] Gerçek Zamanlı Transkripsiyon: Gerçek zamanlı transkripsiyon kapasitesi eklemek, kullanıcıların canlı ses akışlarını anında yazılı metne dönüştürmelerine olanak tanır. Bu, canlı etkinlikler, toplantılar ve konferanslar için kullanışlı olabilir. Bu özelliğin eklenmesi, düşük gecikme sürelerinin sağlanması ve yüksek doğruluk oranlarının korunması gibi teknik zorlukları içerebilir.

- [ ] Güvenlik ve Gizlilik İyileştirmeleri: Kullanıcı verilerinin güvenliğini ve gizliliğini sağlamak amacıyla, endüstri standardı güvenlik protokolleri ve şifreleme yöntemleri uygulamak. Bu, kullanıcıların kişisel ve hassas verilerini güvende tutabilir ve projenin güvenilirliğini artırabilir.

- [ ] Ölçeklenebilirlik ve Performans Optimizasyonu: Projeyi büyük ses dosyalarını hızlı ve etkili bir şekilde işleyebilecek şekilde ölçeklendirmek. Bu, veri yığınlarının paralel işlenmesi, dağıtık hesaplama ve önbellekleme gibi tekniklerin uygulanmasını içerebilir. Bu iyileştirmeler, projenin daha geniş bir kullanıcı tabanına hizmet etmesine yardımcı olabilir ve kullanıcı deneyimini geliştirebilir.

- [ ] Kullanıcı Arayüzü Geliştirmeleri: Kullanıcı dostu bir web arayüzü oluşturarak, kullanıcıların ses dosyalarını kolayca yüklemelerine, transkripsiyon sonuçlarını görüntülemelerine ve düzenlemelerine olanak tanımak. Bu, kullanıcıların projeyi daha etkili bir şekilde kullanmalarına yardımcı olabilir ve projenin erişilebilirliğini artırabilir.

## Lisans

MIT License

Copyright (c) [2023] [EmreOzdemiroglu]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

