#BÖLÜM 1 Öperatörler ile İşlemler

first_number=float(input("Sadece Sayı Giriniz: "))
second_number=float(input("Sadece Sayı Giriniz: "))

#TOPLAMA
print("İki Sayının toplamı: ",  first_number+second_number)
#ÇIKARMA
print("İki Sayının Farkı: ",  first_number-second_number)
#ÇARPMA
print("İki Sayının Çarpımı: ",  first_number*second_number)
#BÖLME
print("İki Sayının Bölümü: ", "Hiçbir sayı 0'a Bölünemez" if second_number==0  else first_number/second_number)
#MOD ALMA
print("İki Sayının Modu: ", "0 ile Mod alınamaz" if second_number==0  else first_number/second_number)
#ÜST ALMA 
print("İki Sayının Üstü: ",  first_number**second_number)