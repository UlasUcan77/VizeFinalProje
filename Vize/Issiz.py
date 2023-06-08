from Insan import Insan


class Issiz(Insan):
    def __init__(self, tc_kimlik_no, ad, soyad, yas, cinsiyet, uyruk, egitim_durumu, tecrubeler=None):
        super().__init__(tc_kimlik_no, ad, soyad, yas, cinsiyet, uyruk)
        self.egitim_durumu = egitim_durumu
        self.tecrubeler = tecrubeler if tecrubeler is not None else []

    def __str__(self):
        return f"Issiz Bilgileri:\nTC No: {self.tc_kimlik_no}\nAd: {self.ad}\nSoyad: {self.soyad}\nYaş: {self.yas}\nCinsiyet: {self.cinsiyet}\nUyruk: {self.uyruk}\nEğitim Durumu: {self.egitim_durumu}\nTecrübeler: {self.tecrubeler}"
