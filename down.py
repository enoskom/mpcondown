import yt_dlp

def get_format_list(url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [info_dict])
    return formats

def secilen_kalite(formats):
    hedef_height = 720
    # Öncelikle 720p var mı bak
    for f in formats:
        if f.get('height') == hedef_height and f.get('vcodec') != 'none':
            return hedef_height
    
    # Eğer 720p yoksa video codec'i olan en yüksek kaliteyi seç
    video_formats = [f for f in formats if f.get('vcodec') != 'none' and f.get('height') is not None]
    if not video_formats:
        return None
    max_height = max(f.get('height') for f in video_formats)
    return max_height

def indir_yt_dlp(link, secilen_format, height=None):
    if secilen_format == "mp3":
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        ydl_opts = {
            'format': f'bestvideo[height={height}]+bestaudio/best[height={height}]/best',
            'outtmpl': '%(title)s.%(ext)s',
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

if __name__ == "__main__":
    while True:
        try:
            adet = int(input("Kaç tane link gireceksiniz? "))
            if adet > 0:
                break
            else:
                print("Lütfen pozitif bir sayı girin.")
        except ValueError:
            print("Geçersiz sayı, tekrar deneyin.")

    linkler = []
    for i in range(adet):
        link = input(f"{i+1}. linki yapıştırın: ").strip().split('&')[0]
        linkler.append(link)

    secilen_format = ""
    while secilen_format not in ["mp3", "mp4"]:
        secilen_format = input("Hangi formatta indirmek istersiniz? (mp3/mp4): ").strip().lower()

    for i, link in enumerate(linkler, 1):
        print(f"\n{i}. link indiriliyor: {link}")
        if secilen_format == "mp4":
            formats = get_format_list(link)
            height = secilen_kalite(formats)

            if not height:
                print("Uygun video formatı bulunamadı, atlanıyor.")
                continue

            print(f"{height}p kalitesinde (veya mevcut en yüksek) indirme başlatılıyor...")
            indir_yt_dlp(link, secilen_format, height)

        else:
            print("En iyi ses kalitesi ile mp3 formatında indirme başlatılıyor...")
            indir_yt_dlp(link, secilen_format)

        print(f"{i}. link indirildi.")

    print("\n✅ Tüm indirmeler tamamlandı.")
