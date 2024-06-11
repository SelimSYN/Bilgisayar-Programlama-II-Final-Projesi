from personel import Personel

# Personel sınıfından türetilmiş bir Hemsire sınıfı tanımlanıyor
class Hemsire(Personel):
    # Hemsire sınıfının başlatıcı metodu
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        # Üst sınıfın (Personel) başlatıcı metodunu çağırarak ortak özelliklerin atanması
        super().__init__(personel_no, ad, soyad, departman, maas)
        # Hemsire sınıfına ait özellikler atanıyor
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    # Çalışma saati özelliğine erişmek için getter metodu
    def get_calisma_saati(self):
        return self.__calisma_saati

    # Sertifika özelliğine erişmek için getter metodu
    def get_sertifika(self):
        return self.__sertifika

    # Hastane özelliğine erişmek için getter metodu
    def get_hastane(self):
        return self.__hastane

    # Çalışma saati özelliğini güncellemek için setter metodu
    def set_calisma_saati(self, calisma_saati):
        self.__calisma_saati = calisma_saati

    # Sertifika özelliğini güncellemek için setter metodu
    def set_sertifika(self, sertifika):
        self.__sertifika = sertifika

    # Hastane özelliğini güncellemek için setter metodu
    def set_hastane(self, hastane):
        self.__hastane = hastane
    
    # Maaşı artırmak için bir metod
    def maas_arttir(self, artis_yuzdesi):
        # Üst sınıftaki (Personel) maaşı artıran metod çağrılıyor
        super().set_maas(self.get_maas() * (1 + artis_yuzdesi))

    # Nesnenin özelliklerini ve bilgilerini string olarak döndüren özel bir metot
    def __str__(self):
        return f"{super().__str__()}, Çalışma Saati: {self.__calisma_saati}, Sertifika: {self.__sertifika}, Hastane: {self.__hastane}"  
