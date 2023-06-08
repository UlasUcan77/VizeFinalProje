from Insan import Insan

class Calisan(Insan):
    def __init__(self, tc_kimlik_no, ad, soyad, yas, cinsiyet, uyruk, departman, calisma_yili, maas, zam_orani):
        super().__init__(tc_kimlik_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__departman = departman
        self.__calisma_yili = calisma_yili
        self.__maas = maas
        self.__zam_orani = zam_orani

    def get_departman(self):
        return self.__departman

    def set_departman(self, departman):
        self.__departman = departman

    def get_calisma_yili(self):
        return self.__calisma_yili

    def set_calisma_yili(self, calisma_yili):
        self.__calisma_yili = calisma_yili

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def get_zam_orani(self):
        return self.__zam_orani

    def set_zam_orani(self, zam_orani):
        self.__zam_orani = zam_orani

    def get_tecrube(self):
        return self.__calisma_yili

    def zam_hakki(self):
        return self.__maas * self.__zam_orani / 100
    
    def yeni_maas(self):
        zam_miktari = self.__maas * self.__zam_orani / 100
        yeni_maas = self.__maas + zam_miktari
        return yeni_maas