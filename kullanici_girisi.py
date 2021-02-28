import time

real_kullanici_adi = input("Kullanıcı adınızı belirleyiniz :")
real_parola = input("Şifrenizi belirleyiniz :")
hak = 3
while True:
    kullanici_adi =input("Kullanıcı Adı : ")
    parola = input("Parola : ")
    if(kullanici_adi != real_kullanici_adi and parola == real_parola):
        print("Kullanıcı adınızı hatalı girdiniz!")
        hak -= 1
    elif(kullanici_adi == real_kullanici_adi and parola != real_parola):
        print("Parolanızı hatalı girdiniz!")
        hak -= 1
    elif (kullanici_adi != real_kullanici_adi and parola != real_parola):
        print("Kullanıcı adınızı ve parolanızı hatalı girdiniz!")
        hak -= 1
        if  (hak == 0):
            time.sleep(2)
            print("Kullanıcı adınız veya şifrenizden emin olup tekrar deneyiniz !!" )
            break
    else:
        print("Giriş Yapılıyor..")
        time.sleep(1.5)
        print("Sisteme Başarıyla Giriş Yaptınız.")
        break
