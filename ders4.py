# LAMBDA ve MAP KULLANIMI

# Lambda, tek satırda fonksiyon tanımlamak için kullanılan özel bir anahtar
# kelimedir

# Python'da Lambda ile tek satırda fonksiyon tanımlamanın formülü
# lambda parametre:işlem

# lambda = anahtar kelime (tıpkı normal fonksiyon tanımlarken kullandığımız
# def anahtar kelimesi gibi MUTLAKA AMA MUTLAKA OLMALI/YAZILMALI)

# parametre = bir fonksiyona vereceğiniz parametre ya da parametreler
# NOT: birden fazla parametre olması durumunda virgüller birbirinden ayrılır

# işlem ise yapılan işlem ve geriye döndürülen sonuçtur
# gizli bir return varmış gibi düşünülmelidir.


# Normal fonksiyon ile dışarıdan girilen bir sayının karesinin hesaplanması

def kare_al(x):
    
    return x**2

print(f"10 sayısının karesi = {kare_al(10)}")

# Lambda ile dışarıdan girilen bir sayının karesinin hesaplanması
kare_lm = lambda y:y**2
print(f"10 sayısının lambda ile karesinin alınması = {kare_lm(10)}")

# PARAMETRE OLARAK GİRİLEN BİR STR İFADENİN KAÇ HARFTEN/KARAKTERDEN
# OLUŞTUĞUNU BULAN LAMBDA KODU - NORMAL FONKSİYON

def count_char(str_ifade):
    return len(str_ifade)

print(f"Üfeyra Bağcı ismi {count_char('Üfeyra Bağcı')} karakterden oluşur")
print("-"*50)

count_char_lm = lambda str_degisken:len(str_degisken)

print(f"Üfeyra Bağcı ismi {count_char_lm('Üfeyra Bağcı')} karakterden oluşur")

 Girilen bir str ifadenin KELİME SAYISINI hesaplayan lambda ve normal fonk.
# NOT: Üfeyra Bağcı yazdıldığında 2 değerini döndürecek

def count_sentence(str_cumle):
    return len(str_cumle.split())

print(f"Üfeyra Bağcı {count_sentence('Üfeyra Bağcı')} kelimeden oluşur")
print("-"*50)

print("Üfeyra Bağcı".split()) # ['Üfeyra','Bağcı'] şeklinde 2 adet eleman döndürür

print("-"*50)

count_sentence_lambda = lambda x:len(x.split())
print(f"Üfeyra Bağcı {count_sentence_lambda('Üfeyra Bağcı')} kelimeden oluşur")

# Girilen 2 sayının toplamını döndüren fonksiyon

def toplam(a,b):
    return a+b

print(f"5 ve 520 sayılarının toplamı = {toplam(5,520)}")
print("-"*50)

# Girilen 2 sayının toplamını döndüren fonksiyon (LAMBDA İLE)

toplam_lm = lambda x,y:x+y
print(f"540 ve 1520 sayılarının toplamı = {toplam_lm(540,1520)}")

# Girilen 3 adet sayının ortalamasını döndüren fonksiyon (ve lambda kodu)

def ortalama(x,y,z):
    return (x+y+z)/3

print(f"5,6 ve 7 sayılarının ortalaması = {ortalama(5,6,7)}")
print("-"*50)

ortalama_lm = lambda a,b,c:(a+b+c)/3
print(f"5,6 ve 7 sayılarının ortalaması = {ortalama_lm(5,6,7)}")

# LAMBDA İLE IF-ELSE KULLANIMI

# formül aşağıdaki gibidir. (x=parametre)
# lambda x:"TRUE YANITI" if kosul else "ELSE YANITI"

# Girilen sayının tek olması durumunda "TEK", değilse "ÇİFT" yazan lambda kodu

tek_mi_cift_mi = lambda sayi:"ÇİFT" if sayi%2==0 else "TEK"

print(f"16 sayısı {tek_mi_cift_mi(16)} sayıdır")
print("-"*50)
print(f"17 sayısı {tek_mi_cift_mi(17)} sayıdır")

# Girilen 2 sayıdan büyüğünü döndüren lambda
# Girilen 2 sayıdan küçüğünü döndüren lambda

# 2 sayıdan büyük sayıyı bulan lambda

buyuk_sayi = lambda x,y:x if x>y else y
kucuk_sayi = lambda a,b:a if a<b else b

print(f"100 ile 1000 sayısının durumu = {buyuk_sayi(100,1000)} sayısı büyüktür")
print(f"100 ile 1000 sayısının durumu = {kucuk_sayi(100,1000)} sayısı küçük")

# Girilen hava sıcaklığı 30'dan küçükse ılık
# 30 veya 30'dan büyükse sıcak yazan lambda kodu

soguk_ilik_lm = lambda x:"ILIK" if x<30 else "SICAK"

print(f"29 derece için hava = {soguk_ilik_lm(29)}")
print("-"*50)
print(f"30 derece için hava = {soguk_ilik_lm(30)}")
print("-"*50)
print(f"31 derece için hava = {soguk_ilik_lm(31)}")

# Girilen 3 sayı arasında en büyük sayıyı döndüren lambda kodu

buyuk_uc_sayi = lambda x,y,z:x if x>y and x>z else(y if y>z else z)

print(f"70,60,50 için en büyük sayı = {buyuk_uc_sayi(70,60,50)}")
print("-"*50)
print(f"50,60,40 için en büyük sayı = {buyuk_uc_sayi(50,60,40)}")
print("-"*50)
print(f"70,60,500 için en büyük sayı = {buyuk_uc_sayi(70,60,500)}")
print("-"*50)
print(f"70,70,70 için en büyük sayı = {buyuk_uc_sayi(70,70,70)}")
#if x>y and x>z:
#    return x
#else:
#    if y>z:
#        return y
#    else:
#        return z

# Girilen 3 sayı arasında en büyük sayıyı döndüren lambda kodu

buyuk_uc_sayi = lambda x,y,z:x if x>y and x>z else(y if y>z else ("hepsi eşittir" if x==y and y==z else z))

print(f"70,60,50 için en büyük sayı = {buyuk_uc_sayi(70,60,50)}")
print("-"*50)
print(f"50,60,40 için en büyük sayı = {buyuk_uc_sayi(50,60,40)}")
print("-"*50)
print(f"70,60,500 için en büyük sayı = {buyuk_uc_sayi(70,60,500)}")
print("-"*50)
print(f"70,70,70 için en büyük sayı = {buyuk_uc_sayi(70,70,70)}")

#if x>y and x>z:
#    return x
#else:
#    if y>z:
#        return y
#    else:
#        return z

# 0 ile 5 derece arası soğuk
# 6 ile 15 derece arası ılık
# 16 ile 25 derece arası sıcak
# 26 ile 40 derece arası çok sıcak
# hiç biri değilse tanımsız değer

hava_durumu_lm = lambda x:"SOĞUK" if 0<=x<=5 else("ILIK" if 6<=x<=15 else("SICAK" if 16<=x<=25 else("ÇOK SICAK" if 26<=x<=40 else "TANIMSIZ DEĞER")))

print(f"5 derece için hava = {hava_durumu_lm(5)}")
print("-"*50)
print(f"13 derece için hava = {hava_durumu_lm(13)}")
print("-"*50)
print(f"22 derece için hava = {hava_durumu_lm(22)}")
print("-"*50)
print(f"35 derece için hava = {hava_durumu_lm(35)}")
print("-"*50)
print(f"41 derece için hava = {hava_durumu_lm(41)}")

# 91 ile 100 için AA
# 81 ile 90 için BA
# 71 ile 80 için BB
# 61 ile 70 için CB
# 51 ile 60 için CC
# 50 ve altı için FF


harf_notu = lambda x:"AA" if 91<=x<=100 else("BA" if 81<=x<=90 else("BB" if 71<=x<=80 else("CB" if 61<=x<=70 else("CC" if 51<=x<=60 else "FF") )))

print(f"95 için harf notu = {harf_notu(95)}")
print("*"*50)
print(f"81 için harf notu = {harf_notu(81)}")
print("*"*50)
print(f"79 için harf notu = {harf_notu(79)}")
print("*"*50)
print(f"70 için harf notu = {harf_notu(70)}")
print("*"*50)
print(f"55 için harf notu = {harf_notu(55)}")
print("*"*50)
print(f"50 için harf notu = {harf_notu(50)}")

harf_notu_2 = lambda x:"AA" if 91<=x<=100 else "BA" if 81<=x<=90 else"BB" if 71<=x<=80 else"CB" if 61<=x<=70 else"CC" if 51<=x<=60 else "FF" 

print(f"95 için harf notu = {harf_notu_2(95)}")
print("*"*50)
print(f"81 için harf notu = {harf_notu_2(81)}")
print("*"*50)
print(f"79 için harf notu = {harf_notu_2(79)}")
print("*"*50)
print(f"70 için harf notu = {harf_notu_2(70)}")
print("*"*50)
print(f"55 için harf notu = {harf_notu_2(55)}")
print("*"*50)
print(f"50 için harf notu = {harf_notu_2(50)}")

# lambda ile bir değerin karesini alan fonksiyon yazabilirsiniz
# Ancak, bu fonksiyonu itere edilebilir (iterable) bir yapıya (örneğin: liste)
# uygulamak istiyorsanız. Yani o yapının bir elemanına değil de tüm elemanlarına
# uygulamak istiyorsanız MUTLAKA AMA MUTLAKA MAP, REDUCE, FILTER fonksiyonlarından
# birini kullanırsınız
# NOT: hepsinin kullanım amacı ayrıdır

# MAP KULLANIMI

# söz dizimi formülü (syntax)

# degisken = list(map(lambda x:x**2,gercek_liste))
# degisken artık sonuçları hesaplanmış bir listedir

# yukarıdaki söz diziminde bir listedeki tüm elemanların karesini hesaplayıp
# bunları da başka bir listeye ekleyen kod bulunmaktadır.

my_list_1 = [x for x in range(1,11)]

result_list_1 = list(map(lambda x:x**2,my_list_1))

print(f"Orijinal Liste = {my_list_1}")
print("-"*50)
print(f"Karesi alınmış liste = {result_list_1}")

# 1'den 10'a kadar olan bir liste ile 
# 11'den 20'ye kadar olan başka bir listede
# bu iki listedeki aynı indeksteki değerleri toplayıp döndüren lambda kodu
# NOT: iki parametre kullanılacak ve iki adet gerçek liste yan yana parametre
# olarak verilecek

my_list_2 = [x for x in range(1,11)]
my_list_3 = [x for x in range(11,21)]

result_list_2 = list(map(lambda x,y:x+y,my_list_2,my_list_3))

print(f"Orijinal_Liste_1 = {my_list_2}")
print("-"*50)
print(f"Orijinal_Liste_2 = {my_list_3}")
print("-"*50)
print(f"Toplam_Liste = {result_list_2}")

my_fonk = lambda x:x**2

bos_liste = []

for i in my_list_1:
    bos_liste.append(my_fonk(i))
print(bos_liste)

calisanlar = {"furkan":65000,"ahmet":50000,"tuğçe":58000,"leyla":68000,
             "seda":72000,"cengiz":23000}

# bir dictionary veri yapısında tutulan maaşlara %30 zam yapan lambda kodu
# dictionary.items() => ('key',value) => örneğin ('furkan',65000) = deger aşağıdaki
# deger[0] = key bilgisi
# deger[1] = value bilgisi. BU İKİ DURUM PYTHON'DA ASLA AMA ASLA DEĞİŞMEZ!!!

zamli_dict = dict(map(lambda deger:(deger[0],deger[1]*1.3),calisanlar.items()))

print(f"calisanlar.items() (Orijinal) = {calisanlar.items()}")
print("-"*50)
deneme = list(calisanlar.items())
print(f"calisanlar.items()[0] = {deneme[0]}")
print(f"calisanlar.items()[0][0] = {deneme[0][0]}")
print(f"calisanlar.items()[0][1] = {deneme[0][1]}")
print("-"*50)
print(f"zamli_dict.items() = {zamli_dict.items()}")

kisiler = {"ahmet":17,"mehmet":23,"hakan":28,"elif":15,"tuba":19,
          "yusuf":21,"tuğçe":22,"leyla":16}

# yukarıdaki verilen kişiler ve onların yaşlarını analiz edin:
# yaşı 18'den küçük olanlar için isim bilgisi, ÇOCUKTUR yazacak
# 18 ve üzeri için de isim bilgisi, YETİŞKİNDİR yazacak
# Örneğin, ahmet 17 yaşında olduğu için ahmet, ÇOCUKTUR yazacak
# lambda ile kodu yazın

yas_list = list(map(lambda deger:f"{deger[0]}, {'ÇOCUKTUR' if deger[1]<18 else 'YETİŞKİNDİR'}",kisiler.items()))

print(f"Orijinal Sözlük = {kisiler.items()}")
print("-"*50)
print(f"İşlenmiş Sözlük = {yas_list}")

kisiler = {"ahmet":17,"mehmet":23,"hakan":28,"elif":15,"tuba":19,
          "yusuf":21,"tuğçe":22,"leyla":16}

# yukarıdaki verilen kişiler ve onların yaşlarını analiz edin:
# yaşı 18'den küçük olanlar için isim bilgisi, ÇOCUKTUR yazacak
# 18 ve üzeri için de isim bilgisi, YETİŞKİNDİR yazacak
# Örneğin, ahmet 17 yaşında olduğu için ahmet, ÇOCUKTUR yazacak
# lambda ile kodu yazın

yas_dict = dict(map(lambda deger:(deger[0], 'ÇOCUKTUR' if deger[1]<18 else 'YETİŞKİNDİR'),kisiler.items()))

yas_dict=dict(map(lambda deger:(deger[0],"ÇOCUKTUR")if deger[1]<18 else (deger[0],"YETİŞKİNDİR"),kisiler.items()))
print(yas_dict)

print(f"Orijinal Sözlük = {kisiler.items()}")
print("-"*50)
print(f"İşlenmiş Sözlük = {yas_dict}")


