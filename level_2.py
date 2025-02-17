#BÖLÜM 2 DÖGÜLER İLE UYGULAMALAR

number=int(input("Sayı Giriniz :"))
total=0
i=1
#Negatif Olma durumu
if number<0:
   while(number!=i):
    total +=i
    i-=1


# 0 Olma Durumu
elif number==0:
  total=0


#Pozitif Olma durumu
else:
  while(number!=i):
   total +=i
   i+=1




print(total)