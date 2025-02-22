# List Comprehension
# Normalde diğer programlama dillerin yerleşik veri yapılarının kullanımı
# Python'a göre oldukça daha fazla kod gerektirir
# Python'da tüm bu işlemler diğer dillere göre daha basit, kolay ve sade iken
# yine Python içerisinde belli kullanım kalıplarıyla bu kullanımlar daha
# kısa hale getirebilir.
# List Comprehension, normalde birkaç satır kodla yapılan işlemlerin tek
# satırda yazılmasını ifade eder.

# Python'da 1'den 100'e kadar olan sayıları içeren bir liste tanımlayın
my_list = []
type(my_list)

my_list = []

# for değişken_adı in range(başlangıç_değeri, bitiş_değeri)

for i in range(1,101):
    my_list.append(i)

print(my_list)

# List Comprehension (LC) ile aynı işlemi yapma
# (1'den 100'e kadar (100 de dahil) sayıları listeye ekleme)

# [değişken_adı for değişken_adı in range(başlangıç_değeri, bitiş_değeri)]
# [burada değişkenin geriye dönüş değeri söz konusu (ilk) aşamada]
my_list_1_lc = [x for x in range(1,101)]
print(my_list_1_lc)

# For döngüsünün 3 kullanımı vardır:
# 1.) for i in range(bitiş_değeri)
# döngü içerisindeki parantezde tek değer varsa bu değer varsayılan olarak
# bitiş değeri olarak kabul edilir, başlangıç değeri de sıfır kabul edilir

# 2.) for i in range(başlangıç_değeri,bitiş_değeri)
# başlangıç_değeri'nden bitiş_değeri-1'e kadar yazdırır

# 3.) for i in range(başlangıç, bitiş, artış miktarı)
# başlangıç değerinden başlar, bitiş değeri-1'e kadar
# artış miktarı kadar aritmetik bir şekilde artırarak ilerler

# if kullanmadan 0'dan 100'e kadar (100'de dahil) sadece çift sayıları
# yazdıran kod

# for i in range(0,101,2)

# 1'den 100'e kadar olan her sayının 5 katını içeren liste
# Normal kod ile:

my_list_3 = []

for i in range(1,101):
    #i = i*5
    #i *= 5
    my_list_3.append(i*5)

print(my_list_3)

# bir listeye birden fazla eleman eklemek için:
# my_list_3.append([i,j,k,l,])

print("-"*50)

my_list_lc_3 = [5*x for x in range(1,101)]
print(my_list_lc_3)

# her sayının 5 katının 3 fazlasını tutan liste (1'den 100'e kadar)
# my_list_lc_3 = [(5*x)+3 for x in range(1,101)]

# LC'lerin if ile kullanımı
# 1'den 100'e kadar olan tek sayıları tutan liste (Normal kod ile yazın)

my_list_4 = []
# i%2==1 eşittir i%2 != 0
for i in range(1,101):
    if i%2 != 0:
        my_list_4.append(i)

print(my_list_4)

# LC yöntemi ile if kullanımı
# formül:
# [değişken for değişken in range() if değişken_ve_işlem]

print("-"*50)

my_list_4_lc = [x for x in range(1,101) if x%2!=0]
print(my_list_4_lc)

# 1 ile 500 arasında (500'de dahil) 2'ye ve 6'ya tam bölünen ama 8'e tam
# bölünmeyen sayılar için "Uygundur" değeri yazdıran liste

# Normal kod ile:

my_list_5 = []

for i in range(1,501):
    if i%2==0 and i%6==0 and i%8!=0:
        my_list_5.append(f"{i} sayısı uygundur")
        #my_list_5.append([i," sayısı uygundur"])

print(my_list_5)

# Normal kod:

my_list_6 = []

for i in range(1,11):
    if i%2==0:
        my_list_6.append("Çift")
    else:
        my_list_6.append("Tek")

print(my_list_6)
#LC ile if-else kullanımı
# formül:
# [değişken if şartı değişken else for değişken in range()]

# 1'den 10'a kadar (10'da dahil) olan tek sayılar için "Tek" yazan
# çift sayılar için "çift" yazan liste
print("-"*50)

my_list_6_lc = ["Tek" if x%2!=0 else "Çift" for x in range(1,11)]
print(my_list_6_lc)

gecici_liste_1 = ["Burdur","Mehmet","Akif","Ersoy","Üniversitesi","YBS","ZTYO"]

# bu listedeki tüm elemanların tamamını büyük harfle yazıp 
# yeni bir listeye ekleyen kodu yazın (normal kod ve list comprehension)

# Normal kod:

my_list_7 = []

for deger in gecici_liste_1:
    my_list_7.append(deger.upper().replace("I","İ"))

print(my_list_7)

print("-"*50)

my_list_7_lc = [x.upper().replace("I","İ") for x in gecici_liste_1]
print(my_list_7_lc)

# 1 ile 100 arasındaki tek sayıların negatif halini çift sayıların
# karesini tutan listeyi LC ile yazınız

# Normal Kod:

my_list_8 = []
for i in range(1,101):
    if i%2==0:
        my_list_8.append(i**2)
    else:
        my_list_8.append(-i)# i*(-1)

print(my_list_8)

print("-"*8)

my_list_8_lc = [x**2 if x%2==0 else -x for x in range(1,101)]

print(my_list_8_lc)

# List Comprehension'da iç içe for kullanımı

# Dış döngü 1'den 5'e kadar (5'te dahil)
# iç döngü 6'dan 10'a kadar (10'da dahil) olmak üzere
# tüm sayıların çarpım sonucunu tutan liste
# Sonuç tek ise sonucu eklesin

# LC

my_list_10_lc = [x*y for x in range(1,6) for y in range(6,11) if (x*y)%2!=0]
print(my_list_10_lc)


# Yukarıdaki sonuçlar içerisinden sadece 21'den büyük, 45'ten küçük veya eşit
# olan sonuçları tutan listeyi LC ile yazın

my_list_11_lc = [x*y for x in range(1,6) for y in range(6,11) if (x*y)%2!=0 and (x*y)>21 and (x*y)<=45]
print(my_list_11_lc)

# Dictionary veri yapısı key:value şeklinde çalışan tek veri tipidir

my_notes = {"furkan":58,"ahmet":73,"yusuf":20,"tuba":13,"tuğçe":85,"ali":50}

# Notları 50'den büyük olan öğrencilerin ismini getiren LC kodunu yazın
# my_notes.key() anahtarları getirir
# my_notes.values() değerleri getirir
# my_notes.items() önce anahtarı sonra değeri getirir (2 değer döndürür)



#LC

my_list_12_lc = [anahtar for anahtar,deger in my_notes.items() if deger>50]
print(my_list_12_lc)

for i in my_notes.items():
    print(i)
