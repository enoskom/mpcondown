# 🎥 mpcondown

Bu proje, iki farklı ama birbirini tamamlayıcı Python aracından oluşur:

1. **download down.py  (yt-dlp tabanlı)**  
   - YouTube videolarını `.mp3` veya `.mp4` formatında indirmenizi sağlar.
   - Otomatik olarak en uygun kaliteyi seçer (varsayılan 720p, yoksa en yüksek mevcut kalite).
   
2. **Frame Extractor fram.py (OpenCV tabanlı)**  
   - Yerel bir video dosyasından belirli bir zaman aralığında kareleri çıkarır.
   - Her kareyi `.jpg` formatında zaman damgalı bir klasöre kaydeder.

---

## 🧰 Gereksinimler

Aşağıdaki Python kütüphanelerinin yüklü olması gerekir:

```bash
pip install yt-dlp opencv-python

