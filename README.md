## Parmak Sayma (Canlı Kamera)

Bu proje, bilgisayarınızın kamerasını açarak elinizi algılar ve parmaklarınızla gösterdiğiniz sayıyı gerçek zamanlı olarak tespit eder. OpenCV, MediaPipe ve NumPy kütüphanelerini kullanır.

### Başlangıç
1. Python 3.9+ kurulu olduğundan emin olun.
2. İsterseniz izole bir ortam oluşturun:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows için: .venv\\Scripts\\activate
   ```
3. Bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

### Çalıştırma
```bash
python src/finger_counter.py
```
- `q` tuşuna basarak uygulamadan çıkabilirsiniz.

### Nasıl Çalışır?
- MediaPipe `Hands` modeli avuç yönünü ve 21 eklem noktasını çıkarır.
- Gelen çerçeveye göre parmak eklemleri analiz edilir; her parmak için açık/kapalı kararı verilir.
- Tespit edilen sayı ve FPS bilgisi ekranda gösterilir.

### İpuçları
- İyi aydınlatılmış bir ortamda kullanın.
- Elinizi kameraya paralel ve görünür olacak şekilde tutmaya çalışın.
- Eğer sahnede birden fazla el varsa, ilk tespit edilen el kullanılır.

### Lisans
Bu proje MIT lisansı ile sunulmuştur.
