# Ortalama-Varyans-Standart Sapma Hesaplayıcısı

def ortalama(liste):
    return sum(liste) / len(liste)

def varyans(liste):
    ortalama_deger = ortalama(liste)
    toplam = 0
    for i in liste:
        toplam += (i - ortalama_deger) ** 2
    return toplam / len(liste)

def standart_sapma(liste):
    return varyans(liste) ** 0.5

sayilar = [3, 5, 8, 12, 15]

print("Sayılar: ", sayilar)
print("Ortalama: ", ortalama(sayilar))
print("Varyans: ", varyans(sayilar))
print("Standart Sapma: ", standart_sapma(sayilar))
