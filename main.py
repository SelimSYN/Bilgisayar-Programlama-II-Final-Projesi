import pandas as pd
from doktor import Doktor
from hemsire import Hemsire
from hasta import Hasta
from personel import Personel


try:
    personel1 = Personel(1, "Halil", "Çulha", "Muhasabe", 20000)
    personel2 = Personel(2, "Arda", "Yılmaz", "Ar-Ge", 30500)

    print(f"{personel1.__str__()} \n{personel2.__str__()}\n")
    
    doktor1 = Doktor(3, "Fidan", "Kılıç", "Ortopedi", 40000, "Kırık Cerrahisi", 10, "AKUT Hastanesi")
    doktor2 = Doktor(4, "Fatma", "Ergün", "Kardiyoloji", 45000, "Pediatrik Kardiyoloji", 12, "EKOL Hastanesi")
    doktor3 = Doktor(5, "Ahmet", "Güven", "Nöröloji", 60000, "İnme ve Vasküler Nöroloji", 4, "KAPU Hastanesi")

    print(f"{doktor1.__str__()} \n{doktor2.__str__()} \n{doktor3.__str__()} \n")

    hemsire1 = Hemsire(6, "Onur", "Kağan", "Pediatri", 25000, 10, "Neonatoloji", "Karşıyaka Hastanesi")
    hemsire2 = Hemsire(7, "Cansu", "Demir", "Yoğun Bakım", 20500, 8, "Nefrolog", "Fenerbahçe Hastanesi")
    hemsire3 = Hemsire(8, "Ayşe", "Keskin", "Acil", 18000, 9, "Travma Cerrahı", "KSK Hastanesi")

    print(f"{hemsire1.__str__()} \n{hemsire2.__str__()} \n{hemsire3.__str__()} \n")

    hasta1 = Hasta(1, "Anıl", "Kara", "1998-02-03", "Enfeksiyon", "Normal")
    hasta2 = Hasta(2, "Ali", "Koç", "1986-07-30", "Kırık", "Özel")
    hasta3 = Hasta(3, "Aziz", "Yıldırım", "2001-10-05", "Grip", "Özel")

    print(f"{hasta1.__str__()} \n{hasta2.__str__()} \n{hasta3.__str__()} \n")

    data = {
            "personel_no": [personel1.get_personel_no(), personel2.get_personel_no(), doktor1.get_personel_no(), doktor2.get_personel_no(), doktor3.get_personel_no(), hemsire1.get_personel_no(), hemsire2.get_personel_no(), hemsire3.get_personel_no(), 0, 0, 0],
            "ad": [personel1.get_ad(), personel2.get_ad(), doktor1.get_ad(), doktor2.get_ad(), doktor3.get_ad(), hemsire1.get_ad(), hemsire2.get_ad(), hemsire3.get_ad(), hasta1.get_ad(), hasta2.get_ad(), hasta3.get_ad()],
            "soyad": [personel1.get_soyad(), personel2.get_soyad(), doktor1.get_soyad(), doktor2.get_soyad(), doktor3.get_soyad(), hemsire1.get_soyad(), hemsire2.get_soyad(), hemsire3.get_soyad(), hasta1.get_soyad(), hasta2.get_soyad(), hasta3.get_soyad()],
            "dogum_tarihi": [0, 0, 0, 0, 0, 0, 0, 0, hasta1.get_dogum_tarihi(), hasta2.get_dogum_tarihi(), hasta3.get_dogum_tarihi()],           
            "departman": [personel1.get_departman(), personel2.get_departman(), doktor1.get_departman(), doktor2.get_departman(), doktor3.get_departman(), hemsire1.get_departman(), hemsire2.get_departman(), hemsire3.get_departman(), 0, 0, 0],
            "maas": [personel1.get_maas(), personel2.get_maas(), doktor1.get_maas(), doktor2.get_maas(), doktor3.get_maas(), hemsire1.get_maas(), hemsire2.get_maas(), hemsire3.get_maas(), 0, 0, 0],
            "Uzmanlik Alanlari:": [0, 0, doktor1.get_uzmanlik(), doktor2.get_uzmanlik(), doktor3.get_uzmanlik(), 0, 0, 0, 0, 0, 0],
            "deneyim_yili": [0, 0, doktor1.get_deneyim_yili(), doktor2.get_deneyim_yili(), doktor3.get_deneyim_yili(), 0, 0, 0, 0, 0, 0],
            "calisma_saati": [0, 0, 0, 0, 0, hemsire1.get_calisma_saati(), hemsire2.get_calisma_saati(), hemsire3.get_calisma_saati(), 0, 0, 0],
            "sertifika": [0, 0, 0, 0, 0, hemsire1.get_sertifika(), hemsire2.get_sertifika(), hemsire3.get_sertifika(), 0, 0, 0],
            "hastane": [0, 0, doktor1.get_hastane(), doktor2.get_hastane(), doktor3.get_hastane(), hemsire1.get_hastane(), hemsire2.get_hastane(), hemsire3.get_hastane(), 0, 0, 0],
            "hasta_no": [0, 0, 0, 0, 0, 0, 0, 0, hasta1.get_hasta_no(), hasta2.get_hasta_no(), hasta3.get_hasta_no()],
            "hastalik": [0, 0, 0, 0, 0, 0, 0, 0, hasta1.get_hastalik(), hasta2.get_hastalik(), hasta3.get_hastalik()],
            "tedavi": [0, 0, 0, 0, 0, 0, 0, 0, hasta1.get_tedavi(), hasta2.get_tedavi(), hasta3.get_tedavi()]
        }
       
    datafr = pd.DataFrame(data)
    datafr['dogum_tarihi'] = pd.to_datetime(datafr['dogum_tarihi'])

    doktor_sayisi = datafr[datafr['Uzmanlik Alanlari:'] != 0].groupby('Uzmanlik Alanlari:').size()
    print(f"Toplam Doktor sayısı: {sum(doktor_sayisi)} \n{doktor_sayisi.to_string(dtype=False)} \n")

    bes_yil_doktor = datafr[(datafr['deneyim_yili'] > 5) & (datafr['deneyim_yili'] != 0)].shape[0]
    print(f"5 yıldan daha fazla deneyime sahip doktorların sayısı: {bes_yil_doktor}\n")

    hastalar = datafr[datafr['hasta_no'] != 0]
    yeni_hastalar = hastalar.sort_values(by=['ad'])
    print(f"Alfabetik sıralanmış hasta listesi: {yeni_hastalar}\n")

    maas_7000 = datafr[datafr['maas'] > 7000]
    print(f"Maaşı 7000 TL üzerinde olan personeller: {maas_7000}\n")

    dogum_1990 = datafr[datafr['dogum_tarihi'] >= '1990-01-01']
    print(f"1990 sonrası doğan hastalar: {dogum_1990}\n")


    yeni_datafr = datafr[['ad', 'soyad', 'departman', 'maas', 'Uzmanlik Alanlari:', 'deneyim_yili', 'hastalik', 'tedavi']]
    print(f"Yeni DataFrame: {yeni_datafr}\n")
  
except Exception:
    print(f"Bir hata oluştu:")