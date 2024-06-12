from personel import Personel
from hemsire import Hemsire
from doktor import Doktor
from hasta import Hasta
import pandas as pd

# Hata kontrolü için try-except bloğu
try:
    # Personel sınıfından iki nesne oluştur
    personel_1 = Personel(1, "Veli", "Arslan", "Hademe", 6000)
    personel_2 = Personel(2, "Tuğran", "Yılmaz", "Laborant", 20500)

    # Personel nesnelerini yazdır
    print(f"{personel_1.__str__()} \n{personel_2.__str__()}\n")
    


    # Doktor sınıfından üç nesne oluştur
    doktor_1 = Doktor(3, "Serkan", "Seyhan", "Dahiliye", 100000, "Dahiliye", 10, "Kadın Doğum Hastanesi")
    doktor_2 = Doktor(4, "Fatma", "Ergün", "Kardiyoloji", 65000, "Yetişkin Kardiyoloji", 12, "Aydın Hastanesi")
    doktor_3 = Doktor(5, "Mihriban", "Gül", "Kardiyoloji", 80000, "Çocuk Kardiyoloji", 4, "EGE Hastanesi")

    # Doktor nesnelerini yazdır
    print(f"{doktor_1.__str__()} \n{doktor_2.__str__()} \n{doktor_3.__str__()} \n")



    # Hemşire sınıfından üç nesne oluştur
    hemsire_1 = Hemsire(6, "Ali", "Veli", "Dahiliye", 15000, 10, "KBB", "Denizli Hastanesi")
    hemsire_2 = Hemsire(7, "Mahmut", "Yılmaz", "Acil", 20500, 7, "Serumcu", "Aydın Hastanesi")
    hemsire_3 = Hemsire(8, "Emre", "Kaan", "Kadın Doğum", 18000, 8, "Ebe", "Nazilli Hastanesi")

    # Hemşire nesnelerini yazdır
    print(f"{hemsire_1.__str__()} \n{hemsire_2.__str__()} \n{hemsire_3.__str__()} \n")



    # Hasta sınıfından üç nesne oluştur
    hasta_1 = Hasta(1, "Demir", "Semerci", "1968-02-13", "Enfeksiyon", "Normal")
    hasta_2 = Hasta(2, "Umut", "Bulut", "1956-07-20", "Kırık", "Özel")
    hasta_3 = Hasta(3, "Emre", "Eren", "2011-10-05", "Su Çiçeği", "Özel")

    # Hasta nesnelerini yazdır
    print(f"{hasta_1.__str__()} \n{hasta_2.__str__()} \n{hasta_3.__str__()} \n")



    # Verileri bir sözlükte birleştir
    data_list = {
            "personel_no": [personel_1.get_personel_no(), personel_2.get_personel_no(), doktor_1.get_personel_no(), doktor_2.get_personel_no(), doktor_3.get_personel_no(), hemsire_1.get_personel_no(), hemsire_2.get_personel_no(), hemsire_3.get_personel_no(), 0, 0, 0],
            "ad": [personel_1.get_ad(), personel_2.get_ad(), doktor_1.get_ad(), doktor_2.get_ad(), doktor_3.get_ad(), hemsire_1.get_ad(), hemsire_2.get_ad(), hemsire_3.get_ad(), hasta_1.get_ad(), hasta_2.get_ad(), hasta_3.get_ad()],
            "soyad": [personel_1.get_soyad(), personel_2.get_soyad(), doktor_1.get_soyad(), doktor_2.get_soyad(), doktor_3.get_soyad(), hemsire_1.get_soyad(), hemsire_2.get_soyad(), hemsire_3.get_soyad(), hasta_1.get_soyad(), hasta_2.get_soyad(), hasta_3.get_soyad()],
            "dogum_tarihi": [0, 0, 0, 0, 0, 0, 0, 0, hasta_1.get_dogum_tarihi(), hasta_2.get_dogum_tarihi(), hasta_3.get_dogum_tarihi()],           
            "departman": [personel_1.get_departman(), personel_2.get_departman(), doktor_1.get_departman(), doktor_2.get_departman(), doktor_3.get_departman(), hemsire_1.get_departman(), hemsire_2.get_departman(), hemsire_3.get_departman(), 0, 0, 0],
            "maas": [personel_1.get_maas(), personel_2.get_maas(), doktor_1.get_maas(), doktor_2.get_maas(), doktor_3.get_maas(), hemsire_1.get_maas(), hemsire_2.get_maas(), hemsire_3.get_maas(), 0, 0, 0],
            "uzmanlik": [0, 0, doktor_1.get_uzmanlik(), doktor_2.get_uzmanlik(), doktor_3.get_uzmanlik(), 0, 0, 0, 0, 0, 0],
            "sertifika": [0, 0, 0, 0, 0, hemsire_1.get_sertifika(), hemsire_2.get_sertifika(), hemsire_3.get_sertifika(), 0, 0, 0],
            "deneyim_yili": [0, 0, doktor_1.get_deneyim_yili(), doktor_2.get_deneyim_yili(), doktor_3.get_deneyim_yili(), 0, 0, 0, 0, 0, 0],
            "calisma_saati": [0, 0, 0, 0, 0, hemsire_1.get_calisma_saati(), hemsire_2.get_calisma_saati(), hemsire_3.get_calisma_saati(), 0, 0, 0],
            "hastane": [0, 0, doktor_1.get_hastane(), doktor_2.get_hastane(), doktor_3.get_hastane(), hemsire_1.get_hastane(), hemsire_2.get_hastane(), hemsire_3.get_hastane(), 0, 0, 0],
            "hasta_no": [0, 0, 0, 0, 0, 0, 0, 0, hasta_1.get_hasta_no(), hasta_2.get_hasta_no(), hasta_3.get_hasta_no()],
            "hastalik": [0, 0, 0, 0, 0, 0, 0, 0, hasta_1.get_hastalik(), hasta_2.get_hastalik(), hasta_3.get_hastalik()],
            "tedavi": [0, 0, 0, 0, 0, 0, 0, 0, hasta_1.get_tedavi(), hasta_2.get_tedavi(), hasta_3.get_tedavi()]
        }
    
    # Sözlükten data_frameame oluştur
    data_frame = pd.DataFrame(data_list)
    


    # Uzmanlık alanlarına göre doktor sayılarını hesapla ve yazdır
    doktor_sayisi = data_frame[data_frame['uzmanlik'] != 0].groupby('uzmanlik').size()
    print(f"Toplam Hekim sayısı: {sum(doktor_sayisi)} \n{doktor_sayisi.to_string(dtype=False)} \n")


    # 5 yıldan fazla deneyime sahip doktorların sayısını hesapla ve yazdır
    bes_yil_doktor = data_frame[(data_frame['deneyim_yili'] != 0) & (data_frame['deneyim_yili'] > 5)].shape[0]
    print(f"Deneyimi 5 yıldan fazla olan doktor sayısı: {bes_yil_doktor}\n")


    # Hastaları al ve adlarına göre alfabetik sırala
    hastalar = data_frame[data_frame['hasta_no'] != 0]
    yeni_hastalar = hastalar.sort_values(by=['ad'])
    print(f"Alfabetik sıraya göre hasta listesi:\n {yeni_hastalar}\n")


    # Maaşı 7000 TL üzerinde olan personelleri al ve yazdır
    maas_7000 = data_frame[data_frame['maas'] > 7000]
    print(f"Maaşı 7000 TL üzerinde olan personeller:\n {maas_7000}\n")


    # Doğum tarihlerini datetime formatına çevir
    data_frame['dogum_tarihi'] = pd.to_datetime(data_frame['dogum_tarihi'])


    # 1990 sonrası doğan hastaları al ve yazdır
    dogum_1990 = data_frame[data_frame['dogum_tarihi'] >= '1990-01-01']
    print(f"1990 yılından sonra doğan hastalar:\n {dogum_1990}\n")


    # Yeni bir data_frameame oluştur ve bazı sütunları seç
    yeni_data_frame = data_frame[['ad', 'soyad', 'departman', 'maas', 'uzmanlik', 'deneyim_yili', 'hastalik', 'tedavi']]
    print(f"Yeni data_frameame:\n {yeni_data_frame}\n")
  
  
except Exception:
    print(f"Bir hata oluştu:") 