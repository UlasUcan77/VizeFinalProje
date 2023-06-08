from Calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self, tc_kimlik_no, ad, soyad, yas, cinsiyet, uyruk, departman, tecrube, maas, tesvik_primi, zam_hakki):
        super().__init__(tc_kimlik_no, ad, soyad, yas, cinsiyet, uyruk, departman, tecrube, maas, zam_hakki)
        self.tesvik_primi = tesvik_primi

    def zam_hakki(self):
        return (self.get_maas() % self.get_tecrube()) * 5 + self.tesvik_primi

    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrube: {self.get_tecrube()} yıl\nYeni Maas: {self.zam_hakki()}"
