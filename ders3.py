# Fonksiyonlar
# Programlamadaki kullanımı matematikteki kullanımıyla birebir aynıdır
# parametreler, işlemler, değer aralıkları, sonuç döndürme
# yukarıdakiler bir fonksiyonun en temel bileşenlerindendir (sonuç döndürme,
# parametre kabul etme olmasa da olabilir)

# 1 sayısının 4 katının 3 fazlası = 7
# 3 sayısının 4 katının 3 fazlası = 15
# 5 sayısının 4 katının 3 fazlası = 23
# 7 sayısının 4 katının 3 fazlası = 31
# 9 sayısının 4 katının 3 fazlası = 39

# x € Z+ [1, 9] x+2 olmak üzere f(x) = (4*x)+3

for x in range(1,10,2):
    print((x*4)+3)

# Fonksiyonlar 4 farklı şekilde çalıştırılabilir
# Parametreli, Parametresiz
# Değer döndüren, değer döndürmeyen
# Kod yazarken gerçek dünyada en sık karşılaşılan fonksiyon türleri:
# parametreli fonksiyonlarda tanımlama şöyledir
# fonksiyon_adı(parametre1,parametre2,...,parametre_n)
# değer döndüren fonksiyonlar da mutlaka ama mutlaka return anahtar kelimesiyle
# bitirilir. Bu ifade bir nevi "exit" anlamı taşır
# fonksiyon içerisindeki tüm işlemler, parametrelere göre yapılır
# derleyici en son return ifadesini ve onun return ettiği değişkeni görür
# bundan sonra fonksiyonu sonlandırır

# vize ve final notunu parametre olarak alan ve vizenin yüzde 40'ı
# finalin %60'ının toplamı 50 ve ya 50'den büyükse GEÇTİNİZ yazan
# değilse KALDINIZ yazan fonksiyon (geriye değer döndürmeyen)

# NOT: eğer istenirse daha parametre tanımlama aşamasında parametrelerin
# tipleri de belirtilebilir. Hatta bu yaklaşım daha iyi olacaktır.
# Hem kod okuma açısından hem de o tip'in getirdiği tüm özellikleri daha
# en başta kullanma açısından

def notlar_non_return(vize:int, final:int):
    son_not = (vize*0.4)+(final*0.6)
    if son_not>=50:
        print("GEÇTİNİZ")
    else:
        print("KALDINIZ")

gecici_non_return = notlar_non_return(40,60)
print(gecici_non_return)


# Geriye değer döndüren fonksiyon ile aynı görevin yazımı

def notlar_return(vize:int, final:int):
    son_not = (vize*0.4)+(final*0.6)
    if son_not>=50:
        return "GEÇTİNİZ"
    else:
        return "KALDINIZ"

gecici_return = notlar_return(40,60)
print(gecici_return)

gecici_return = gecici_return + " geriye değer döndürdü"
print(f"Return yapılan fonksiyon çıktısı = {gecici_return}")

gecici_non_return = gecici_non_return + "geriye değer döndürmedi"
print(f"Return yapılmayan fonksiyon çıktısı = {gecici_non_return}")

# Geriye değer döndüren int temelli fonksiyon
# Parametre olarak bir sayı alan ve bu sayının tek mi çift mi 
# olduğunu yazdıran fonksiyon

def tek_mi_cift_mi(number:int):
    if number%2==0:
        return "ÇİFT"
    else:
        return "TEK"

sonuc_1 = tek_mi_cift_mi(15)
print(sonuc_1)

# Parametre olarak girilen iki sayının toplamını return eden fonksiyonu yazınız

def topla(x:int,y:int):
    return x+y

my_result_1 = topla(58,63)
print(my_result_1)

def cift_ise(par_cift:int):
    return (par_cift*-4)+5

def tek_ise(par_tek:int):
    return par_tek**2

if my_result_1%2!=0: # sonucum tek ise
    print(tek_ise(my_result_1))
else: # sonucum çift ise aşağıdaki fonksiyon benim sonuç parametremle çalışır
    print(cift_ise(my_result_1))
 
# eğer fonksiyondan dönen sonuç tek ise bu sonucun başka bir fonksiyonla
# karesini hesaplayıp geriye döndürün

# çift ise yine başka bir fonksiyonla -4 katının 5 fazlasını hesaplayıp
# geriye döndürün


# Dışarıdan parametre olarak bir numara listesi alan
# bu listedeki tek elemanları yeni bir listeye
# çift elemanları yeni başka bir listeye ekleyip
# return olarak bu iki listeyi döndüren fonksiyon

my_num_list = [x for x in range(0,101)]

def list_tek_cift(gecici_liste:list):
    
    my_tek_list, my_cift_list = [], []

    for deger in gecici_liste:
        if deger%2==0:
            my_cift_list.append(deger)
        else:
            my_tek_list.append(deger)

    return my_tek_list, my_cift_list

tek_sayilar, cift_sayilar = list_tek_cift(my_num_list)

print(f"Tek sayıların listesi = {tek_sayilar}")
print(f"Çift sayıların listesi = {cift_sayilar}")

# Dışarıdan alınan 1'den 100'e kadar sayıları içeren bir listedeki
# 2, 3, 4 ve 5'e tam bölünen sayıları farklı listelere ekleyip
# bu dört listeyi return eden fonksiyonu yazınız

my_num_list_2 = [x for x in range(1,101)]

def coklu_liste(gecici_liste_2:list):
    mod_2, mod_3, mod_4, mod_5 = [], [], [], []
    for i in gecici_liste_2:
        if i%2==0:
            mod_2.append(i)
        if i%3==0:
            mod_3.append(i)
        if i%4==0:
            mod_4.append(i)
        if i%5==0:
            mod_5.append(i)
    return mod_2, mod_3, mod_4, mod_5

liste_2, liste_3, liste_4, liste_5 = coklu_liste(my_num_list_2)

print(f"2'ye tam bölünenler = {liste_2}")
print(f"3'e tam bölünenler = {liste_3}")
print(f"4'e tam bölünenler = {liste_4}")
print(f"5'e tam bölünenler = {liste_5}")

# bir fonksiyon aşağıdaki söz dizimiyle tanımlanır
# NOT: parametre alan ve geriye değer döndüren
def fonksiyon_adı(parametre_1,parametre_2):
    #işlemler burda yapılır
    #işlemler bittikten sonra sonuç return edilir
    # son satırda return edilmesi lazım
    # return'den sonra herhangi bir kod YAZILMAMALIDIR
    return sonuc
# bir fonksiyon şöyle çalıştırılır
# fonksiyon_adı(parametre_1, parametre_2)
# bir fonksiyondan dönen değeri tutmak için şu söz dizimi izlenir
degisken_sonuc = fonksiyon_adı(gercek_parametre_1, gercek_parametre_2)
# bu sonucu yazdırmak/görüntülemek için de aşağıdaki kod yazılır
print(degisken_sonuc)

# dışarıdan parametre olarak girilen bir listedeki
# tüm sayıların karesini bir listeye
# 2 katını başka bir listeye ekleyip döndüren fonksiyonu yazınız

my_list_3 = [x for x in range(1,11)]

def mat_islem(gecici_list_4:list):
    liste_iki_kati, liste_karesi = [], []
    for i in gecici_list_4:
        liste_iki_kati.append(2*i)
        liste_karesi.append(i**2)
    return liste_iki_kati, liste_karesi

my_list_iki_kati, my_list_karesi = mat_islem(my_list_3)

print(f"Listedeki elemanların 2 katı = {my_list_iki_kati}")
print(f"Listedeki elemanların karesi = {my_list_karesi}")

deger_1 = "kabak"

print(f"Orijinal Kelime = {deger_1}")
print(f"Kelimenin Ters çevrilmiş Hali = {deger_1[::-1]}")
print(f"Cevap = {deger_1==deger_1[::-1]}")

my_list_4 = ["ses","kelek","tuz","şeker","kek","süt","kabak"]

# Yukarıda verilen listeyi parametre olarak alan ve bu listedeki
# baştan ve tersten yazılışı aynı olan kelimeleri bulup, bunları
# yeni bir listeye ekleyip döndüren fonksiyonu yazın

def esittir(gecici_list_5:list):
    liste_esittir = []

    for kelime in gecici_list_5:
        if kelime==kelime[::-1]:
            liste_esittir.append(kelime)
    return liste_esittir

my_result_5 = esittir(my_list_4)

print(f"Orijinal Liste = {my_list_4}")
print(f"Aynı kelimeler = {my_result_5}")

my_list_6 = ["BURDUR","Mehmet","akif","ERSOY","üniversitesi",
            "Bucak","ZTYO"]

# yukarıdaki listeyi parametre olarak alan
# ve bu listedeki tamamı büyük harflerle yazılmış kelimeleri tespit edip, 
# yeni bir listeye ekleyip döndüren fonksiyon

#"Mehmet"!="MEHMET"
#"BURDUR"=="BURDUR

def buyukluk_kontrolu(gecici_list_6:list):
    liste_buyuk = []
    for kelime in gecici_list_6:
        if kelime==kelime.upper():
            liste_buyuk.append(kelime)
    return liste_buyuk

my_liste_buyuk = buyukluk_kontrolu(my_list_6)

print(f"Orijinal Liste = {my_list_6}")
print(f"İşlenmiş Liste = {my_liste_buyuk}")

# Farklı veri yapılarını kullanma

deneme_1 = {"ali":26,"ahmet":13,"mehmet":18,"cengiz":32,"ayşe":25,"elif":12}

print(f"Sadece key'leri yazdırma = {deneme_1.keys()}")
print("-"*50)
print(f"Sadece value'leri yazdırma = {deneme_1.values()}")
print("-"*50)
print(f"Hem key'i hem de value'yi aynı anda birlite yazdırma = {deneme_1.items()}")
print("-"*50)
print(f"Tek bir key'in değerini yazdırma Örneğin ali key'ine ait değeri yazdırma")
print(deneme_1["ali"])

deneme_1 = {"ali":22000,"ahmet":13000,"mehmet":100000,"cengiz":32000,
            "ayşe":25000,"elif":12000}
# Dışarıdan parametre olarak verilen bir dictionary' içerisinde sadece maaş bilgisi
# 25000'den küçük olanlara %50 zam yapan, 25000 ve üzerine %30 zam yapan ve bunları
# bir listede döndüren fonksiyon

def maas_zam(gecici_sozluk:dict):
    zamli_maas = []
    for deger in gecici_sozluk.values():
        if deger>=25000:
            #zamli_maas.append(deger*1.3) # %30'unu direkt hesaplar
            zamli_maas.append(deger+(deger*0.3)) # 30'unu dolaylı olarak hesaplar
        else:
            zamli_maas.append(deger+(deger*0.5))
    return zamli_maas

yeni_maaslar = maas_zam(deneme_1)

print(f"Orijinal maaşlar = {deneme_1.values()}")
print(f"Zamlı maaşlar = {yeni_maaslar}")

