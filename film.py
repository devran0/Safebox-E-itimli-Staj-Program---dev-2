class Film:
    def __init__(self, ad, yonetmen, yil):
        self.ad = ad
        self.yonetmen = yonetmen
        self.yil = yil

    def __str__(self):
        return f"Film Adı: {self.ad}, Yönetmen: {self.yonetmen}, Yıl: {self.yil}"

class FilmArsivi:
    def __init__(self, dosya):
        self.dosya = dosya

    def film_ekle(self, film):
        with open(self.dosya, "a") as dosya:
            dosya.write(f"{film.ad},{film.yonetmen},{film.yil}\n")

    def film_ara(self, anahtar_kelime):
        sonuclar = []
        with open(self.dosya, "r") as dosya:
            for satir in dosya:
                ad, yonetmen, yil = satir.strip().split(",")
                film = Film(ad, yonetmen, yil)
                if anahtar_kelime.lower() in film.ad.lower() or anahtar_kelime.lower() in film.yonetmen.lower():
                    sonuclar.append(film)
        return sonuclar

dosya_adi = "filmler.txt"

arsiv = FilmArsivi(dosya_adi)

while True:
    print("\n1. Film Ekle")
    print("2. Film Ara")
    print("3. Çıkış")

    secim = input("Seçiminizi yapın (1-3): ")

    if secim == "1":
        ad = input("Film adını girin: ")
        yonetmen = input("Yönetmen adını girin: ")
        yil = input("Yılını girin: ")
        film = Film(ad, yonetmen, yil)
        arsiv.film_ekle(film)
        print("Film başarıyla eklendi!")
    elif secim == "2":
        anahtar_kelime = input("Film adı veya yönetmen adı girin: ")
        sonuclar = arsiv.film_ara(anahtar_kelime)
        if sonuclar:
            print("Arama Sonuçları:")
            for film in sonuclar:
                print(film)
        else:
            print("Arama sonucu bulunamadı.")
    elif secim == "3":
        break
    else:
        print("Geçersiz seçim!")