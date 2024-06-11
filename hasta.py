# Hasta sınıfı tanımlanıyor
class Hasta:
    # Hasta sınıfının başlatıcı metodu
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        # Hasta özellikleri başlatılıyor
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi

    # Hasta numarasına erişmek için getter metodu
    def get_hasta_no(self):
        return self.__hasta_no
    
    # Ad özelliğine erişmek için getter metodu
    def get_ad(self):
        return self.__ad
    
    # Soyad özelliğine erişmek için getter metodu
    def get_soyad(self):
        return self.__soyad
    
    # Doğum tarihi özelliğine erişmek için getter metodu
    def get_dogum_tarihi(self):
        return self.__dogum_tarihi
    
    # Hastalık özelliğine erişmek için getter metodu
    def get_hastalik(self):
        return self.__hastalik
    
    # Tedavi özelliğine erişmek için getter metodu
    def get_tedavi(self):
        return self.__tedavi
    
    # Hasta numarasını güncellemek için setter metodu
    def set_hasta_no(self, hasta_no):
        self.__hasta_no = hasta_no

    # Ad özelliğini güncellemek için setter metodu
    def set_ad(self,ad):
        self.__ad = ad

    # Soyad özelliğini güncellemek için setter metodu
    def set_soyad(self, soyad):
        self.__soyad = soyad

    # Doğum tarihi özelliğini güncellemek için setter metodu
    def set_dogum_tarihi(self, dogum_tarihi):
        self.__dogum_tarihi = dogum_tarihi

    # Hastalık özelliğini güncellemek için setter metodu
    def set_hastalik(self, hastalik):
        self.__hastalik = hastalik

    # Tedavi özelliğini güncellemek için setter metodu
    def set_tedavi(self, tedavi):
        self.__tedavi = tedavi

    # Tedavi süresini hesaplayan bir metod
    def tedavi_suresi_hesapla(self):
        if self.__hastalik == "Hasta":
            if self.__tedavi == "Normal" : 
               return "6 gün" 
            elif self.__tedavi == "Özel" :
                return "8 gün"
        elif self.__hastalik == "Su Çiçeği":
            if self.__tedavi == "Normal" : 
               return "8 gün" 
            elif self.__tedavi == "Özel" :
                return "10 gün"
        elif self.__hastalik == "Enfeksiyon":
            if self.__tedavi == "Normal" : 
               return "3 gün" 
            elif self.__tedavi == "Özel" :
                return "5 gün"            
        else:
            return "Hastanın net bir tedavi süresi yoktur."

    # Nesnenin özelliklerini ve bilgilerini string olarak döndüren özel bir metot
    def __str__(self):
        return f"Hasta No: {self.__hasta_no}, Ad: {self.__ad}, Soyad: {self.__soyad}, Doğum Tarihi: {self.__dogum_tarihi}, Hastalık: {self.__hastalik}, Tedavi: {self.__tedavi}"
