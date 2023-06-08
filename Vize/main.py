import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka



insan1 = Insan("12345678901", "Ulaş", "Uçan", 19, "Erkek", "Türk")
insan2 = Insan("98765432109", "Azra", "Demir", 25, "Kadın", "Türk")


issiz1 = Issiz("13579246801", "Ali", "Er", 35, "Erkek", "Türk", "Edebiyat", None)
issiz2 = Issiz("24680135792", "Rıfat", "Aydın", 40, "Erkek", "Türk", "Mühendislik", None)
issiz3 = Issiz("11111111111", "Melike", "Kara", 27, "Kadın", "Türk", "Ekonomi", None)


calisan1 = Calisan("98765432123", "Ahmet", "Demir", 30, "Erkek", "Türk", "Bilgi Teknolojileri", 5, 5000, 2)
calisan2 = Calisan("56789012345", "Ayşe", "Öztürk", 28, "Kadın", "Türk", "Pazarlama", 3, 8000, 3)
calisan3 = Calisan("67890123456", "Muhammed", "Sıcakyüz", 35, "Erkek", "Türk", "Muhasebe", 8, 10000, 5)


mavi_yaka1 = MaviYaka("55555555555", "Mehmet", "Saraç", 40, "Erkek", "Türk", "Üretim", 2, 6000, 0.2, 1)
mavi_yaka2 = MaviYaka("77777777777", "Cem", "Yılmaz", 27, "Erkek", "Türk", "Komedyen", 4, 10000, 0.5, 2)
mavi_yaka3 = MaviYaka("99999999999", "Ahmet", "Eryiğit", 30, "Erkek", "Türk", "Kalite Kontrol", 6, 12000, 0.3, 3)


beyaz_yaka1 = BeyazYaka("22222222222", "Utku", "Kürkçü", 25, "Kadın", "Türk", "Finans", 2, 8000, 500, 1)
beyaz_yaka2 = BeyazYaka("44444444444", "Ömer", "Tekin", 35, "Erkek", "Türk", "İnsan Kaynakları", 4, 15000, 1500, 5)
beyaz_yaka3 = BeyazYaka("66666666666", "Mustafa", "Kılıç", 40, "Erkek", "Türk", "Programcı", 6, 20000, 3000, 3)

nesneler = [insan1, insan2, issiz1, issiz2, issiz3, calisan1, calisan2, calisan3, mavi_yaka1, mavi_yaka2, mavi_yaka3,
            beyaz_yaka1, beyaz_yaka2, beyaz_yaka3]


nesneler_df = pd.DataFrame({
    "Tip": [type(calisan).__name__ for calisan in nesneler],
    "TC Kimlik No": [calisan.get_tc_kimlik_no() for calisan in nesneler],
    "Ad": [calisan.get_ad() for calisan in nesneler],
    "Soyad": [calisan.get_soyad() for calisan in nesneler],
    "Yaş": [calisan.get_yas() for calisan in nesneler],
    "Cinsiyet": [calisan.get_cinsiyet() for calisan in nesneler],
    "Uyruk": [calisan.get_uyruk() for calisan in nesneler],
    "Departman": [calisan.get_departman() if isinstance(calisan, (Calisan, MaviYaka, BeyazYaka)) else None for calisan in
                   nesneler],
    "Tecrübe": [calisan.get_tecrube() if isinstance(calisan, (Calisan, MaviYaka, BeyazYaka)) else None for calisan in
                nesneler],
    "Maaş": [calisan.get_maas() if isinstance(calisan, (Calisan, MaviYaka, BeyazYaka)) else None for calisan in nesneler],
    "Zam Hakkı": [calisan.zam_hakki() if isinstance(calisan, (Calisan, MaviYaka, BeyazYaka)) else None for calisan in
                  nesneler],
    "Yeni Maas": [calisan.yeni_maas() if isinstance(calisan, (Calisan, MaviYaka, BeyazYaka)) else None for calisan in
                  nesneler]
})

print("a) DataFrame:")
print(nesneler_df)
print()

departmanlar = nesneler_df["Departman"].unique()

ortalama_maaslar = {}
for departman in departmanlar:
    maaslar = nesneler_df[nesneler_df["Departman"] == departman]["Maaş"]
    ortalama_maaslar[departman] = maaslar.mean()

print("b) Departmana Göre Ortalama Maaşlar:")
for departman, maas in ortalama_maaslar.items():
    print(departman, ":", maas)

nesneler_sirali = nesneler_df.sort_values("Tecrübe")
print("c) Tecrübeye Göre Sıralanmış DataFrame:")
print(nesneler_sirali)
print()

nesneler_sirali_yeni_maas = nesneler_df.sort_values("Yeni Maas", ascending=True)
print("d) Yeni Maaşa Göre Sıralanmış DataFrame (Küçükten Büyüğe):")
print(nesneler_sirali_yeni_maas)
print()

nesneler_sirali_yeni_maas_ters = nesneler_df.sort_values("Yeni Maas", ascending=False)
print("e) Yeni Maaşa Göre Sıralanmış DataFrame (Büyükten Küçüğe):")
print(nesneler_sirali_yeni_maas_ters)
