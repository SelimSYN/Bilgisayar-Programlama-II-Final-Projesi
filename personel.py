# Personel sınıfı tanımlanıyor
class Personel:
    # Personel sınıfının başlatıcı metodu
    def __init__(self, personel_no, ad, soyad, departman, maas):
        # Personel özellikleri başlatılıyor
        self.__personel_no = personel_no
        self.__ad = ad
        self.__soyad = soyad
        self.__departman = departman
        self.__maas = maas

    # Personel numarasına erişmek için getter metodu
    def get_personel_no(self):
        return self.__personel_no

    # Personel numarasını güncellemek için setter metodu
    def set_personel_no(self, personel_no):
        self.__personel_no = personel_no

    # Ad özelliğine erişmek için getter metodu
    def get_ad(self):
        return self.__ad

    # Ad özelliğini güncellemek için setter metodu
    def set_ad(self, ad):
        self.__ad = ad

    # Soyad özelliğine erişmek için getter metodu
    def get_soyad(self):
        return self.__soyad

    # Soyad özelliğini güncellemek için setter metodu
    def set_soyad(self, soyad):
        self.__soyad = soyad

    # Departman özelliğine erişmek için getter metodu
    def get_departman(self):
        return self.__departman

    # Departman özelliğini güncellemek için setter metodu
    def set_departman(self, departman):
        self.__departman = departman

    # Maaş özelliğine erişmek için getter metodu
    def get_maas(self):
        return self.__maas

    # Maaş özelliğini güncellemek için setter metodu
    def set_maas(self, maas):
        self.__maas = maas

    # Nesnenin özelliklerini ve bilgilerini string olarak döndüren özel bir metot
    def __str__(self):
        return f"Personel No: {self.__personel_no}, Ad: {self.__ad}, Soyad: {self.__soyad}, Departman: {self.__departman}, Maaş: {self.__maas}"  
