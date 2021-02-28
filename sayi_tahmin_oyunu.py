import random
import time

print("Hoşgeldiniz..!!")
deger = int(input("1 ile Kaç arasında olan sayıyı doğru bilmeye çalışmak istiyorsunuz? :"))
sayi = random.randint(1,deger)
can = 5

while True:
    tahmin = int(input("Tahmininiz : "))
    if tahmin < sayi:
        time.sleep(1.5)
        print("Alçakta kaldınız YÜKSELİN !! \n1 Can Kaybettiniz..")
        can -= 1
    elif tahmin > sayi:
        time.sleep(1.5)
        print("Fazla yüksekten uçuyorsunuz ALÇALIN !! \n1 Can Kaybettiniz..")
        can -= 1
    else:
        time.sleep(1.5)
        print("Doğru Cevabı bildiniz",sayi)
        break
    if can == 0:
        time.sleep(0.5)
        print("Tahmin Hakkınız Kalmadı..Sayımız:",sayi)
        break