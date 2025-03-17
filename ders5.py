# Filter ve Reduce fonksiyonları
# Tıpkı Map fonksiyonu gibi bu iki fonksiyonda iterable (örneğin liste gibi) 
# nesneler üzerinde çok güçlü işlemleri tek satır kodla yapmaya yarar.
# Filter, kullanımı map ile birebir aynıdır (syntax yapısı vs.)
# Ancak, map'ten önemli bir farkı vardır:
# Sadece şart ifadelerinden sonra True olan değerlerin kendisini döndürür
# NOT: map True da olsa False da olsa hepsini döndürür



kare_al = lambda x: x**2
print(kare_al(5))

# örnek map kullanımı

my_list_1 = [x for x in range(1,11)] #1'den 10'a kadar olan sayılar listesi

liste_kare = list(map(lambda x:x**2,my_list_1))

print(f"Orijinal Liste = {my_list_1}")
print(f"-"*50)
print(f"Karesi alınmış Liste = {liste_kare}")

# -10'dan başlayıp +10'a kadar olan sayıları barındıran listeyi
# list comp ile oluşturun 

my_list_2 = [x for x in range(-10,11)]

# bu listedeki sadece pozitif olan elemanları başka bir listeye alın
# Not: bu ikinci işlemi hem normal fonksiyon hem map hem de filter ile yazın

def pozitif_sayilar(deneme:list):
    bos_liste = []

    for sayi in deneme:
        if sayi>=0:
            bos_liste.append(sayi)
    return bos_liste

pozitif_fonk = pozitif_sayilar(my_list_2)
# Aynı işlemi map ile yapma
pozitif_map = list(map(lambda x:x>=0,my_list_2))
# Aynı işlemi filter ile yapma
pozitif_filter = list(filter(lambda x:x>=0,my_list_2))

print(f"Normal Fonksiyon sonucu = {pozitif_fonk}")       
print(f"-"*50)
print(f"Map Fonksiyonu sonucu = {pozitif_map}")           # Koşula uyanları True dödürüp uymayanları False döndürür
print(f"-"*50)
print(f"Filter Fonksiyonu sonucu = {pozitif_filter}")     #Sadece koşula uyan değerleri döndürür

# -10'dan başlayıp +10'a kadar olan sayıları barındıran listeyi
# list comp ile oluşturun 

my_list_2 = [x for x in range(-10,11)]

# bu listedeki sadece negatif ve çift olan elemanları başka bir listeye alın
# Not: bu ikinci işlemi hem normal fonksiyon hem map hem de filter ile yazın

def pozitif_sayilar(deneme:list):
    bos_liste = []

    for sayi in deneme:
        if sayi<0 and sayi%2==0:
            bos_liste.append(sayi)
    return bos_liste

pozitif_fonk = pozitif_sayilar(my_list_2)
# Aynı işlemi map ile yapma
pozitif_map = list(map(lambda x:x<0 and x%2==0,my_list_2))
# Aynı işlemi filter ile yapma
pozitif_filter = list(filter(lambda x:x<0 and x%2==0,my_list_2))

print(f"Normal Fonksiyon sonucu = {pozitif_fonk}")
print(f"-"*50)
print(f"Map Fonksiyonu sonucu = {pozitif_map}")
print(f"-"*50)
print(f"Filter Fonksiyonu sonucu = {pozitif_filter}")

my_list_3 = ["Burdur","Bucak","Mehmet Akif Ersoy","Üniversitesi","ZTYO",
            "Yönetim Bilişim Sistemleri","BST","MFY"]

# yukarıdaki listede yer alan ve kelime sayısı 7 ve üzeri olan kelimeleri
# döndüren liste (normal fonksiyon, map ve filter ile)

# Normal fonksiyon olarak yazımı
#@decorator_fonk_adi

def kelime_sayisi(deneme:list):
    bos_liste = []
    for kelime in deneme:
        if len(kelime)>=7:
            bos_liste.append(kelime)
    return bos_liste


kelime_fonk = kelime_sayisi(my_list_3)
kelime_map = list(map(lambda x:len(x)>=7,my_list_3))
kelime_filter = list(filter(lambda x:len(x)>=7,my_list_3))

print(f"Normal Fonksiyon sonucu = {kelime_fonk}")
print(f"-"*50)
print(f"Map Fonksiyonu sonucu = {kelime_map}")
print(f"-"*50)
print(f"Filter Fonksiyonu sonucu = {kelime_filter}")

my_list_3 = ["Burdur","Bucak","Mehmet Akif Ersoy","Üniversitesi","ZTYO",
            "Yönetim Bilişim Sistemleri","BST","MFY"]

# yukarıdaki listede yer alan ve kelime sayısı 7 ve üzeri olan ve 
# içerisinde boşluk karakteri olmayan kelimeleri
# döndüren liste (normal fonksiyon, map ve filter ile)

# Normal fonksiyon olarak yazımı
#@decorator_fonk_adi

def kelime_sayisi(deneme:list):
    bos_liste = []
    for kelime in deneme:
        if len(kelime)>=7 and " " not in kelime:
            bos_liste.append(kelime)
    return bos_liste

kelime_fonk = kelime_sayisi(my_list_3)
kelime_map = list(map(lambda x:len(x)>=7 and " " not in x,my_list_3))
kelime_filter = list(filter(lambda x:len(x)>=7 and " " not in x,my_list_3))

print(f"Normal Fonksiyon sonucu = {kelime_fonk}")
print(f"-"*50)
print(f"Map Fonksiyonu sonucu = {kelime_map}")
print(f"-"*50)
print(f"Filter Fonksiyonu sonucu = {kelime_filter}")

my_list_3 = ["Burdur","Bucak","Mehmet Akif Ersoy","Üniversitesi","ZTYO",
            "Yönetim Bilişim Sistemleri","BST","MFY"]

# yukarıdaki listede yer alan ve kelime sayısı 7 ve üzeri olan ve 
# içerisinde boşluk karakteri olmayan kelimeleri tersten yazdıran
# döndüren liste (normal fonksiyon, map ve filter ile)

# Normal fonksiyon olarak yazımı
#@decorator_fonk_adi

def kelime_sayisi(deneme:list):
    bos_liste = []
    for kelime in deneme:
        if len(kelime)>=7 and " " not in kelime:
            kelime = kelime[::-1]
            bos_liste.append(kelime)
    return bos_liste

kelime_fonk = kelime_sayisi(my_list_3)
kelime_map = list(map(lambda x:len(x)>=7 and " " not in x,my_list_3))
kelime_filter = list(filter(lambda x:x[::-1],kelime_fonk))

print(f"Normal Fonksiyon sonucu = {kelime_fonk}")
print(f"-"*50)
print(f"Map Fonksiyonu sonucu = {kelime_map}")
print(f"-"*50)
print(f"Filter Fonksiyonu sonucu = {kelime_filter}")

my_list_3 = ["Burdur","Bucak","Mehmet Akif Ersoy","Üniversitesi","ZTYO",
            "Yönetim Bilişim Sistemleri","BST","MFY"]

# yukarıdaki listede yer alan ve kelime sayısı 7 ve üzeri olan ve 
# içerisinde boşluk karakteri olmayan kelimeleri tersten yazdıran
# döndüren liste (normal fonksiyon, map ve filter ile)

# Normal fonksiyon olarak yazımı
#@decorator_fonk_adi

def kelime_sayisi(deneme:list):
    bos_liste = []
    for kelime in deneme:
        if len(kelime)>=7 and " " not in kelime:
            kelime = kelime[::-1]
            bos_liste.append(kelime)
    return bos_liste

kelime_fonk = kelime_sayisi(my_list_3)
kelime_map = list(map(lambda x:x[::-1] if len(x)>=7 and " " not in x else "",my_list_3))
kelime_filter = list(filter(lambda x:x[::-1] if len(x)>=7 and " " not in x else "",my_list_3))

print(f"Normal Fonksiyon sonucu = {kelime_fonk}")
print(f"-"*50)
print(f"Map Fonksiyonu sonucu = {kelime_map}")
print(f"-"*50)
print(f"Filter Fonksiyonu sonucu = {kelime_filter}")

# Reduce fonksiyonu, map ve filter'in aksine geriye sadece tek bir değer
# döndürür
# map ve filter ise bir liste döndürürdü

# bu nedenle map ve filter list() parantezinde yazılırken reduce kendi
# başına yazılır
# yine map ve filter'dan en önemli farkı MUTLAKA AMA MUTLAKA iki parametre 
# kullanır

# Bunun nedeni, reduce fonksiyonu bir liste içerisinde bir işlem yapıp
# geriye tek bir değer döndürdüğü için yardımcı bir değişkene ihtiyacı olmasıdır

# Örnek, 1'den 1000'e kadar sayıların toplamı (liste içindeki sayılar)
# !reduce fonksiyonu dışarıdan import edilmesi gereken bir fonksiyondur
# !functools isimli kütüphaneye ait bir fonksiyondur 
# !aşağıdaki gibi import edilir

from functools import reduce

my_list_5 = [x for x in range(1,1001)]

toplam = reduce(lambda x,y:x+y,my_list_5)
print(f"1'den 1000'e kadar olan sayıların toplamı = {toplam}")

# Yukarıdaki görevi normal fonksiyon ile yerine getirmek
def klasik_toplam(deneme:list):
    toplam = 0
    for sayi in deneme:
        toplam = toplam + sayi
    return toplam

print("-"*50)
print(f"Normal fonksiyon ile toplam = {klasik_toplam(my_list_5)}")

# Verilen listedeki en büyük sayıyı döndüren reduce kodu

my_list_6 = [-5000,120,45,0,12,-236,586,10000,1402,-83]

# sıralama ya da listeden tek bir değer döndürme işleminde tek parametre
# kullanılanamaz. Çünkü , tek parametre zaten değerin kendisidir
# özellikle karşılaştırma işlemlerinde mutlaka ama mutlaka ikinci bir değere
# ihtiyaç vardır
# Reduce fonksiyonu da geriye tek değer döndürdüğü için DAİMA iki parametreli
# olarak tanımlanır
my_list_6 = [-5000,120,45,0,12,-236,586,10000,1402,-83]

#reduce ile listedeki en büyük elemanı bulan kodu yazın.

en_buyuk_sayi = reduce(lambda x,y:x if x>y else y,my_list_6)
print(f"Orijal Liste = {my_list_6}")
print("-"*50)
print(f"Listedeki en büyük sayı = {en_buyuk_sayi}")

# Faktöriyel kodunu reduce ile yazın
# not 1'den x'e kadar olan listedeki tüm elemanlar üzerinden hesaplayacaksınız

my_list_7 = [x for x in range(1,21)]

faktoriyel = reduce(lambda x,y:x*y,my_list_7)
print(f"20 sayısının faktöriyeli = {faktoriyel}")

my_list_8 = ["Burdur","Bucak","Mehmet Akif Ersoy","Üniversitesi","ZTYO",
            "Yönetim Bilişim Sistemleri","BST","MFY"]
# yukarıdaki listedeki en uzun kelimeyi döndüren reduce kodu

en_uzun_kelime = reduce(lambda x,y:x if len(x)>len(y) else y,my_list_8)
print(f"Orijal Liste = {my_list_8}")
print("-"*50)
print(f"Listedeki en uzun kelime = {en_uzun_kelime}")

my_list_9 = [105,16,206,107,506] # 188 ort

# yukarıdaki listedeki sayıların ortalamasını reduce ile hesaplayın

toplam_sayi = reduce(lambda x,y:x+y,my_list_9)
ortalama = reduce(lambda x,y:x+y,my_list_9)/len(my_list_9)
ortalama_ilk = reduce(lambda x,y:(x+y)/5,my_list_9)

print(f"Listedeki sayıların toplamı = {toplam_sayi}")
print(f"Listedeki elemanların sayısı = {len(my_list_9)}")
print(f"Listedeki elemanların ortalaması = {toplam_sayi/len(my_list_9)}")
print(f"-"*50)
print(f"Reduce ile Ortalama Sonucu = {ortalama}")
print(f"Reduce ile Ortalama Sonucu = {ortalama_ilk}")

def ortalama_dogru(deneme:list):
    toplam = 0
    for x in deneme:
        toplam += x
    return toplam/len(deneme)
print(ortalama_dogru(my_list_9))

def ortalama_yanlis(deneme:list):
    toplam = 0
    for x in deneme:
        toplam = (toplam + x)/5
        #ortalama = toplam/5
    return toplam
print(ortalama_yanlis(my_list_9))



