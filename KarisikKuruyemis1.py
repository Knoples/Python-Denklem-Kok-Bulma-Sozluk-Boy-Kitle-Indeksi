
print("Lütfen Bilinmeyenleri Yazınız")
print("a*x^2+b*x+c")
a= float(input("a => "))
b= float(input("b => "))
c= float(input("c => "))

delta=b**2-4*a*c
if delta > 0:
   x1 = (-b + (((b**2)-(4*a*c)))**(1/2))/(2*a)
   x2 = (-b-(((b**2)-(4*a*c)))**(1/2))/(2*a)
   print(x1)
   print(x2)
elif delta == 0:
     x1 = (-b + (((b**2)-(4*a*c)))**(1/2))/(2*a)
     x2 = (-b-(((b**2)-(4*a*c)))**(1/2))/(2*a)
     print(x1)
     print(x2)
     print("iki kök birbirine eşit")
elif delta < 0:
    print("denklemin gerçek kökü yoktur.")


Sözlük1={}
isim1 = input("Oyuncu 1'in İsmi:" )
soyad1 = input("Oyuncu 1'in Soyadı:")
takımb1= input("Oyuncu 1'in Takım Bilgisi:")
isim2 = input("Oyuncu 2'nin İsmi:" )
soyad2 = input("Oyuncu 2'nin Soyadı:")
takımb2= input("Oyuncu 2'nin Takım Bilgisi:")
isim3 = input("Oyuncu 3'ün İsmi:" )
soyad3 = input("Oyuncu 3'ün Soyadı:")
takımb3= input("Oyuncu 3'ün Takım Bilgisi:")


Sözlük1["Oyuncu 1 İsim:"]= isim1
Sözlük1["Oyuncu 1 Soyad:"]= soyad1
Sözlük1["Oyuncu 1 Takım Bilgisi:"]= takımb1

Sözlük1["\Oyuncu 2 İsim:"]= isim2
Sözlük1["\Oyuncu 2 Soyad:"]= soyad2
Sözlük1["Oyuncu 2 Takım Bilgisi:"]= takımb2

Sözlük1["Oyuncu 3 İsim:"]= isim3
Sözlük1["Oyuncu 3 Soyad:"]= soyad3
Sözlük1["Oyuncu 3 Takım Bilgisi:"]= takımb3


print(Sözlük1)

sözlük2={}
    
boy1 = float(input("Kullanıcı 1'in Boyu (metre cinsinden örnek: 176 santimetre = 1.76 metre):" ))
kilo1 = float(input("Kullanıcı 1'in Kilosu (kilogram cinsinden):"))

boy2 = float(input("Kullanıcı 2'nin Boyu:" ))
kilo2 = float(input("Kullanıcı 2'nin Kilosu:"))

boy3 = float(input("Kullanıcı 3'ün Boyu:" ))
kilo3 = float(input("Kullanıcı 3'ün Kilosu:"))



sözlük2["Kullanıcı 1 Boy:"] = boy1
sözlük2["Kullanıcı 1 Kilo:"] = kilo1

sözlük2["Kullanıcı 2 Boy:"] = boy2
sözlük2["Kullanıcı 2 Kilo:"] = kilo2

sözlük2["Kullanıcı 3 Boy:"] = boy3
sözlük2["Kullanıcı 3 Kilo:"] = kilo2


while True:
    print("Hangi Kullanıcının Beden Kitle İndeksini İstiyorsunuz Kullanıcı 1 için 1, Kullanıcı 2 için 2, Kullanıcı 3 için 3 yazınız\n")
    kullanıcıboy= input("=>")
    
    if kullanıcıboy == "1":
       print((kilo1)/(boy1*boy1))
       break
    elif kullanıcıboy == "2":
       print((kilo2)/(boy2*boy2))
       break
    elif kullanıcıboy == "3":
       print((kilo3)/(boy3*boy3))
       break
    else:
       print("yanlış tuşladınız lütfen tekrar giriniz")
       exit
