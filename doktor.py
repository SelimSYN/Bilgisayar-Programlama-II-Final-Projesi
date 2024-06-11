# Personel modülünden Personel sınıfı çağrılıyor
from personel import Personel

# Doktor sınıfı tanımlanıyor ve Personel sınıfından miras alınıyor
class Doktor(Personel):
    # Doktor sınıfının başlatıcı metodu
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        # Üst sınıfın başlatıcı metodunu çağırarak ortak özelliklerin atanması
        super().__init__(personel_no, ad, soyad, departman, maas)
        # Doktora özgü özellikler atanıyor
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    # Uzmanlık özelliğine erişmek için getter metodu
    def get_uzmanlik(self):
        return self.__uzmanlik

    # Deneyim yılı özelliğine erişmek için getter metodu
    def get_deneyim_yili(self):
        return self.__deneyim_yili

    # Hastane özelliğine erişmek için getter metodu
    def get_hastane(self):
        return self.__hastane

    # Uzmanlık özelliğini güncellemek için setter metodu
    def set_uzmanlik(self, uzmanlik):
        self.__uzmanlik = uzmanlik

    # Deneyim yılı özelliğini güncellemek için setter metodu
    def set_deneyim_yili(self, deneyim_yili):
        self.__deneyim_yili = deneyim_yili

    # Hastane özelliğini güncellemek için setter metodu
    def set_hastane(self, hastane):
        self.__hastane = hastane

    # Maaş artışı hesaplayan bir metod
    def maas_arttir(self, artis_yuzdesi):
        super().set_maas(self.get_maas() * (1 + artis_yuzdesi))

    # Nesnenin özelliklerini ve bilgilerini string olarak döndüren özel bir metot
    def __str__(self):
        return f"{super().__str__()},  Uzmanlık: {self.__uzmanlik},  Deneyim Yılı: {self.__deneyim_yili},  Hastane: {self.__hastane}"
