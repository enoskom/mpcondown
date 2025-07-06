import cv2
import os
import datetime

# Kullanıcıdan video dosyası adı al
video_yolu = input("Lütfen video dosyasının adını girin (örnek: video.mp4): ").strip()

# Video açılır
cap = cv2.VideoCapture(video_yolu)
if not cap.isOpened():
    print("⚠️ Video açılamadı. Dosya adını veya yolunu kontrol et.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
toplam_kare = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
video_suresi = toplam_kare / fps

print(f"🎞 Video FPS: {fps}")
print(f"🕒 Video süresi: {video_suresi:.2f} saniye")

# Zaman giriş kontrolü
while True:
    try:
        baslangic_saniye = float(input("Başlangıç zamanı (saniye): ").strip())
        bitis_saniye = float(input("Bitiş zamanı (saniye): ").strip())
        if baslangic_saniye < 0 or bitis_saniye > video_suresi or baslangic_saniye >= bitis_saniye:
            raise ValueError
        break
    except ValueError:
        print("⚠️ Geçerli bir zaman aralığı girin! (örn: başlangıç < bitiş ve süre içinde)")

# Kaç karede bir kayıt yapılacağı
while True:
    try:
        kare_atla = int(input("Kaç karede bir kaydedilsin? (örn: 1 = her kare): ").strip())
        if kare_atla < 1:
            raise ValueError
        break
    except ValueError:
        print("⚠️ Geçerli bir sayı girin (en az 1)!")

# Zaman damgalı klasör oluştur
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
cikis_klasoru = f'kareler_{timestamp}'
os.makedirs(cikis_klasoru, exist_ok=True)

# Başlangıç ve bitiş kare numaraları
baslangic_kare = int(baslangic_saniye * fps)
bitis_kare = int(bitis_saniye * fps)

# Videoyu başlangıç karesine konumlandır
cap.set(cv2.CAP_PROP_POS_FRAMES, baslangic_kare)

sayac = 0
mevcut_kare = baslangic_kare

# Kareleri kaydet
while mevcut_kare < bitis_kare:
    ret, kare = cap.read()
    if not ret:
        break
    if (mevcut_kare - baslangic_kare) % kare_atla == 0:
        dosya_adi = os.path.join(cikis_klasoru, f'kare_{sayac:05d}.jpg')
        cv2.imwrite(dosya_adi, kare)
        sayac += 1
    mevcut_kare += 1

cap.release()

print(f"\n✅ Toplam {sayac} kare kaydedildi.")
print(f"📁 Kayıt klasörü: {cikis_klasoru}")
print(f"⏱ Aralık: {baslangic_saniye:.2f} - {bitis_saniye:.2f} saniye")
