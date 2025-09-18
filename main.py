def main():
    yasakli_isimler = ["trump", "erdoğan", "recep tayyip erdoğan"]

    # Oyuncu ismi
    isim = input("Oyuncu adınızı giriniz: ").strip().lower()
    if isim in yasakli_isimler:
        print("Daha fazla seçime girme hakkınız yok. Oyun bitmiştir.")
        return
    else:
        print("Oyun başladı hedefiniz verdiğiniz kararlar doğrultusunda seçimi tekrar kazanabilmek\n")

    puan = 0

    # Tur 1
    print("Seçimi kazandınız ilk ne yapacaksınız ?")
    print("1- Halka konuşma yap")
    print("2- Sarayı gez")
    print("3- Kutlama partisi yap")
    print("4- Rakiplerini aşağıla")
    secim = input("Seçiminiz (1-4): ")
    if secim == "1":
        puan += 1
    else:
        puan -= 1

    # Tur 2
    print("\nÜlkede ilk ne yapacaksınız ?")
    print("1- Halkın içinde gez")
    print("2- Kurumları düzenle")
    print("3- Şahsi harcama yap")
    print("4- Bakanlıkları denetle")
    secim = input("Seçiminiz (1-4): ")
    if secim in ["1", "2", "4"]:
        puan += 1
    else:
        puan -= 1

    # Tur 3
    print("\n2. olarak ne yapacaksınız")
    print("1- Vergileri azalt")
    print("2- Vergileri arttır")
    print("3- Dış ülkelerle görüş")
    print("4- Eğitimi geliştir")
    secim = input("Seçiminiz (1-4): ")
    if secim in ["1", "4"]:
        puan += 1
    else:
        puan -= 1

    # Tur 4
    print("\nSeçime az kaldı sıradaki hamleniz")
    print("1- Zorunlu askerliği kaldır")
    print("2- Bedelli askerliği kaldır")
    print("3- Savunma sanayiyi geliştir")
    print("4- Yeni ibadethaneler aç")
    secim = input("Seçiminiz (1-4): ")
    if secim in ["1", "3"]:
        puan += 1
    else:
        puan -= 1

    # Tur 5 (DÜZELTİLDİ: 3. şık artık -1)
    print("\nSeçim çalışmalarına başla")
    print("1- Sokaklarda seçim otobüsü gezdir")
    print("2- Esnafı gez")
    print("3- Azınlık kitleyle ilgilen")
    print("4- Peyzaj çalışmaları yap")
    secim = input("Seçiminiz (1-4): ")
    if secim in ["2", "4"]:
        puan += 1
    else:
        puan -= 1

    # Tur 6
    print("\nSeçim için televizyona çıktınız rakiplerinize ne söyleyeceksiniz ?")
    print("1- Beni kimse yenemez")
    print("2- Bizim vizyonumuzu onlar hayal dahi edemez")
    print("3- Size bir daha zafer yok")
    print("4- Kaybedince üzülmeyin seneye kazanırsınız")
    secim = input("Seçiminiz (1-4): ")
    if secim in ["2", "3"]:
        puan += 1
    else:
        puan -= 1

    # Sonuç
    if puan > 0:
        print("\nTebrikler tekrardan ülkeyi yönetiyorsunuz")
    elif puan < 0:
        print("\nKaybettiniz tekrar deneyin")
    else:
        # Tie-breaker
        print("\nSeçim sonucu şu an 50-50, her şey son hamleye bağlı!")
        print("\nSon hakkınız ne yapacaksınız?")
        print("1- Hiçbir şey yapma")
        print("2- İlk hamleyi rakipten bekle")
        print("3- Halka konuşma yap")
        print("4- Rakibini açık münazaraya çağır")
        secim = input("Seçiminiz (1-4): ")
        if secim in ["3", "4"]:
            print("\nTebrikler tekrardan ülkeyi yönetiyorsunuz")
        else:
            print("\nKaybettiniz tekrar deneyin")


if __name__ == "__main__":
    main()
