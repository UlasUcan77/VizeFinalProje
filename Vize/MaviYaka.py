from Calisan import Calisan

class MaviYaka(Calisan):
    def __init__(self, tc_kimlik_no, ad, soyad, yas, cinsiyet, uyruk, departman, tecrube, maas, yipranma_payi, zam_hakki):
        super().__init__(tc_kimlik_no, ad, soyad, yas, cinsiyet, uyruk, departman, tecrube, maas, zam_hakki)
        self.__yipranma_payi = yipranma_payi

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        try:
            if self.get_tecrube() >= 2 and self.get_tecrube() < 4 and self.get_maas() < 15000:
                return (self.get_maas() % self.get_tecrube()) / 2 + (self.get_yipranma_payi() * 10)
            elif self.get_tecrube() >= 4 and self.get_maas() < 25000:
                return (self.get_maas() % self.get_tecrube()) / 3 + (self.get_yipranma_payi() * 10)
            else:
                return self.get_yipranma_payi() * 10
        except ZeroDivisionError:
            return 0

    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrube: {self.get_tecrube()} yıl\nYeni Maas: {self.zam_hakki()}"
