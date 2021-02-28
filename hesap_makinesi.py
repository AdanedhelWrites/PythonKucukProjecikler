from math import *
import time

def toplama(a,b):
    return a + b
def cikarma(a,b):
    return a - b
def carpma(a,b):
    return a * b
def bolme(a,b):
    return a / b
def mod(a,b):
    return a % b
def karekok(a):
    return a ** 0.5
def kare_al(a):
    return a ** 2
def iki_sayi_kare_al(a,b):
    return a ** b
def yuzde_al(a):
    return a * (1 / 100)
def bir_bolu_kac(a):
    return 1 / a

print("""   
**** Hesap Makinesine Hoşgeldiniz *********
Toplama Yapmak İçin : 1
Çıkartma Yapmak İçin : 2
Çarpma Yapmak İçin  : 3
Bölme Yapmak İçin : 4 
Mod İşlemi için : 5
Karekök İşlemi için : 6
Kare İşlemi için : 7
İki sayının karesi için : 8
Yüzdesini almak için : 9
Bir'i bölmek için : 10
Çıkmak İsterseniz : 0

""")

while True:
    islem=input("Yapmak istediğiniz işlemi seçiniz :")
    if (islem == "0"):
        print("Hoşçakalın !!")
        time.sleep(1)
        break
    elif(islem == "1"):
        a = int(input("1. Sayıyı Giriniz:"))
        b = int(input("2. Sayıyı Giriniz:"))
        time.sleep(1)
        print(toplama(a,b))
    elif(islem == "2"):
        a = int(input("1. Sayıyı Giriniz:"))
        b = int(input("2. Sayıyı Giriniz:"))
        time.sleep(0.5)
        print(cikarma(a,b))
    elif(islem == "3"):
        a = int(input("1. Sayıyı Giriniz:"))
        b = int(input("2.Sayıyı Giriniz:"))
        time.sleep(0.5)
        print(carpma(a,b))
    elif(islem == "4"):
        a = int(input("1. Sayıyı Giriniz:"))
        b = int(input("2. Sayıyı Giriniz:"))
        time.sleep(0.5)
        print(bolme(a,b))
    elif(islem == "5"):
        a = int(input("1. Sayıyı Giriniz:"))
        b = int(input("2. Sayıyı Giriniz:"))
        print(mod(a,b))
    elif(islem == "6"):
        a = int(input("Karekökü Alınacak sayıyı giriniz:"))
        print(karekok(a))
    elif (islem == "7"):
        a = int(input("Karesi alınacak sayıyı giriniz:"))
        print(kare_al(a))
    elif (islem == "8"):
        a = int(input("Alttaki sayıyı giriniz:"))
        b = int(input("Üstteki sayıyı giriniz:"))
        print(iki_sayi_kare_al(a,b))
    elif (islem == "9"):
        a = int(input("Yuzdesi alınacak sayıyı giriniz:"))
        print(yuzde_al(a))
    elif (islem == "10"):
        a = int(input("Bir'i böleceğiniz sayıyı giriniz:"))
        print(bir_bolu_kac(a))
        
    else:
        time.sleep(1)
        print("Geçersiz Bir İşlem Kodladınız Lütfen Geçerli Bir İşlem Kodlayınız")

