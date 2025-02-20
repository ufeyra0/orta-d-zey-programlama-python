# Kullanıcıdan iki adet tamsayı alan ve bu iki sayıyla
# 4 temel işlemi yapan; ayrıca her iki sayının da 5.dereceden
# üssünü alan kodu yazınız...

number_1 = input("Lütfen 1. sayıyı giriniz: ")
number_2 = input("Lütfen 2. sayıyı giriniz: ")

# try-except blokları
# çalışmasını istediğimiz kodu try bloku içerisine yazarız
# bir hata olması durumunda direkt hatayı bize gösteren
# except blokunda da hatayı tanımlarız

# "number_1/number_2" print ile ilk yazılan süslü parantez
# number_1/number_2 ise print ile eşitlikten sonra yazdığımız süslü parentez
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