# Kullanıcıdan iki adet tamsayı alan ve bu iki sayıyla
# 4 temel işlemi yapan; ayrıca her iki sayının da 5.dereceden
# üssünü alan kodu yazınız...

number_1 = input("Lütfen 1. sayıyı giriniz: ")
number_2 = input("Lütfen 2. sayıyı giriniz: ")

# try-except blokları
# çalışmasını istediğimiz kodu try bloku içerisine yazarız
# bir hata olması durumunda direkt hatayı bize gösteren
# except blokunda da hatayı tanımlarız

#45+50 = 95
# / sonucu = 50/5 = 10.0
# // sonucu = 50/5 = int(10.0) = 10
# isdigit() fonksiyonu, değişkenin int tipinde olup olmadığını kontrol eder
# geriye True ya da False olarak 2 farklı yanıt döndürür.
# Eğer değerler int tipinde ise True, değilse False yanıtı döndürür.
try:
    if number_1.isdigit() and number_2.isdigit():
        number_1 = int(number_1)
        number_2 = int(number_2)

        bolme = number_1/number_2
        
        print(f"{number_1}+{number_2} = {number_1+number_2}")
        print(f"{number_1}-{number_2} = {number_1-number_2}")
        print(f"{number_1}*{number_2} = {number_1*number_2}")
        print(f"{number_1}/{number_2} (float tipinde) = {number_1/number_2}")
        print(f"{number_1}/{number_2} (float tipinde  düşük hassasiyet 1) = {number_1/number_2:0.2f}")
        print(f"{number_1}/{number_2} (float tipinde düşük hassasiyet 2) = {bolme:0.2f}")
        print(f"{number_1}//{number_2} (int tipinde) = {number_1//number_2}")
        print(f"{number_1}/{number_2} int() ile dönüştürülmüş hali= {int(number_1/number_2)}")
        print(f"{number_1}**5 = {number_1**5}")
        print(f"{number_2}**5 = {number_2**5}")
    else:
        print("Lütfen 2 sayının da tamsayı olduğundan emin olun")

except Exception as e:
    print(f"Hata = {e}")

# (str işlemi): bir metin içerisindeki cümlede yer alan
# Türkçe karakterleri İngilizce karşılığı ile değiştiren
# kodu yazınız. (Örneğin, Cümlede ç harfi geçiyorsa c yazacak
# Ç harfi geçiyorsa C yazacak)

my_sentence = "Orta Çağ Döneminden beri farklı diller konuşulmaktadır. Üzücü olan şudur kİ bugün yaşadığımız tüm sıkıntıların bir sebebi de dillerin birer birer ölmesidir."

print(f"Orijinal cümle = {my_sentence}")
print("-"*50)

my_sentence = my_sentence.replace("ç","c").replace("Ç","C").replace("ğ","g").replace("Ğ","G").replace("ı","i").replace("İ","I").replace("ö","o").replace("Ö","O").replace("ş","s").replace("Ş","S").replace("ü","u").replace("Ü","U")
""
print(f"İşlenmiş Cümle = {my_sentence}")

my_sentence = "Orta Çağ Döneminden beri farklı diller konuşulmaktadır. Üzücü olan şudur kİ bugün yaşadığımız tüm sıkıntıların bir sebebi de dillerin birer birer ölmesidir."

my_dictionary = {"isim":"Furkan","soyisim":"ATLAN","yas":31,
                "dersler":["Orta Düzey Programlama, Python Programlama"]}

print(f"Dictionary veri yapısının Tüm anahtarları (keys) = {my_dictionary.keys()}")
print("-"*50)
print(f"Dictionary veri yapısının Tüm değerleri (values) = {my_dictionary.values()}")
print("-"*50)
print(f"Dictionary veri yapısının anahtar ve değerleri = {my_dictionary.items()}")
print("-"*50)
print(f"Sadece isim anahtarının değeri = {my_dictionary['isim']}")

my_sentence = "Orta Çağ Döneminden beri farklı diller konuşulmaktadır. Üzücü olan şudur kİ bugün yaşadığımız tüm sıkıntıların bir sebebi de dillerin birer birer ölmesidir."

print(f"Cümlenin orijinal hali = {my_sentence}")

turkish_to_english = {"Ç":"C","ğ":"g","ö":"o"}

for turkish_character, english_character in turkish_to_english.items():
    my_sentence = my_sentence.replace(turkish_character, english_character)

print("-"*50)
print(f"Cümlenin işlenmiş hali = {my_sentence}")

# Girilen bir tamsayının kendisi haricinde tüm tam bölenlerini
# bulan ve bunları bir listeye ekleyip; sonrasında for döngüsü ile
# tek tek gösteren kodu yazınız. NOT: kaç adet tam böleni olduğu
# bilgisini de yazdırınız

my_num_1 = int(input("Lütfen tamsayı giriniz: "))

bolenler = []
sayac = 0

for i in range(1,my_num_1):
    if my_num_1%i==0:
        bolenler.append(i)
        sayac = sayac + 1
        #sayac += 1 # yukarıdaki sayac kodu ile aynı işi yap

print(f"{my_num_1} sayısının {sayac} adet tam böleni bulundu:")
for i in bolenler:
    print(i)
