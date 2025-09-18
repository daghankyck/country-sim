def main():
    print("Select language / Dil seçin:")
    print("1 - English")
    print("2 - Türkçe")
    lang = input("Choice / Seçim: ").strip()

    yasakli_isimler = ["trump", "erdoğan", "recep tayyip erdoğan", "rte"]

    if lang == "1":
        isim = input("Enter your name: ").strip().lower()
    else:
        isim = input("Oyuncu adınızı giriniz: ").strip().lower()

    if isim in yasakli_isimler:
        print("You have no more right to run for election. Game over." if lang == "1"
              else "Daha fazla seçime girme hakkınız yok. Oyun bitmiştir.")
        return
    else:
        print("The game has started! Your goal is to win the election again based on your decisions.\n"
              if lang == "1"
              else "Oyun başladı! Hedefiniz verdiğiniz kararlar doğrultusunda seçimi tekrar kazanabilmek.\n")

    puan = 0

    if lang == "1":
        questions = [
            ("You’ve won the election. What’s your first move?",
             ["Address the nation", "Tour the White House", "Throw a victory party", "Humiliate your rivals"],
             ["1"]),

            ("What will you do next?",
             ["Meet people on the streets", "Reform key institutions", "Authorize personal spending", "Audit the ministries"],
             ["1", "2", "4"]),

            ("What’s your third step?",
             ["Cut taxes", "Raise taxes", "Hold talks with foreign countries", "Improve education"],
             ["1", "4"]),

            ("With elections approaching, what’s next?",
             ["Raise the minimum wage", "Introduce compulsory military service", "Boost the defense industry", "Open new places of worship"],
             ["1", "3"]),

            ("Kick off the campaign:",
             ["Parade the campaign bus through the streets", "Meet with business leaders", "Focus on minority groups", "Build new tax-free prisons"],
             ["2", "4"]),

            ("Live on TV—what do you say to your rivals?",
             ["Nobody can beat me", "Our vision is beyond their imagination", "You will never win again", "Don’t be sad when you lose"],
             ["2", "3"])
        ]

        tie_breaker = (
            "It’s 50–50 right now—everything hinges on your final move!",
            ["Do nothing", "Wait for your rival’s first move", "Address the nation", "Challenge your rival to an open debate"],
            ["3", "4"]
        )

    else:
        questions = [
            ("Seçimi kazandınız, ilk ne yapacaksınız?",
             ["Halka konuşma yap", "Sarayı gez", "Kutlama partisi yap", "Rakiplerini aşağıla"],
             ["1"]),

            ("Ülkede ilk ne yapacaksınız?",
             ["Halkın içinde gez", "Kurumları düzenle", "Şahsi harcama yap", "Bakanlıkları denetle"],
             ["1", "2", "4"]),

            ("2. olarak ne yapacaksınız?",
             ["Vergileri azalt", "Vergileri arttır", "Dış ülkelerle görüş", "Eğitimi geliştir"],
             ["1", "4"]),

            ("Seçime az kaldı, sıradaki hamleniz?",
             ["Asgari ücrete zam yap", "Askerliği zorunlu hale getir", "Savunma sanayiyi geliştir", "Yeni ibadethaneler aç"],
             ["1", "3"]),

            ("Seçim çalışmalarına başla:",
             ["Sokaklarda seçim otobüsü gezdir", "Esnafı gez", "Azınlık kitleyle ilgilen", "Peyzaj çalışmaları yap"],
             ["2", "4"]),

            ("Seçim için televizyona çıktınız, rakiplerinize ne söyleyeceksiniz?",
             ["Beni kimse yenemez", "Bizim vizyonumuzu onlar hayal dahi edemez", "Size bir daha zafer yok", "Kaybedince üzülmeyin"],
             ["2", "3"])
        ]

        tie_breaker = (
            "Seçim sonucu şu an 50-50, her şey son hamleye bağlı!",
            ["Hiçbir şey yapma", "İlk hamleyi rakipten bekle", "Halka konuşma yap", "Rakibini açık münazaraya çağır"],
            ["3", "4"]
        )

    # --- Oyun döngüsü ---
    for q, opts, positives in questions:
        print("\n" + q)
        for i, opt in enumerate(opts, 1):
            print(f"{i}- {opt}")
        secim = input("Seçiminiz (1-4): ").strip()
        if secim in positives:
            puan += 1
        elif secim in ["1", "2", "3", "4"]:
            puan -= 1
        else:
            puan -= 1
            print("Hiçbir şey yapmadığınız için seçimi kaybettiniz" if lang != "1" else "You lost because you did nothing")

    # --- Sonuç ---
    if puan > 0:
        print("\n" + ("Congratulations, you are re-elected!" if lang == "1" else "Tebrikler tekrardan ülkeyi yönetiyorsunuz"))
    elif puan < 0:
        print("\n" + ("You lost the election. Try again." if lang == "1" else "Kaybettiniz. Tekrar deneyin."))
    else:
        print("\n" + tie_breaker[0])
        for i, opt in enumerate(tie_breaker[1], 1):
            print(f"{i}- {opt}")
        secim = input("Seçiminiz (1-4): ").strip()
        if secim in tie_breaker[2]:
            print("\n" + ("Congratulations, you won in tie-breaker!" if lang == "1" else "Tebrikler, son hakla seçildiniz!"))
        else:
            print("\n" + ("You lost in tie-breaker." if lang == "1" else "Son Turda kaybettiniz."))


if __name__ == "__main__":
    main()
