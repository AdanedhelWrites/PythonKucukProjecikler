import time

sys_kullanıcı_adı = input("Kullanıcı adınızı belirleyiniz :")
sys_parola = input("Şifrenizi belirleyiniz :")
hak = 3
while True:
    kullanıcı_adı =input("Kullanıcı Adı : ")
    parola = input("Parola : ")
    if(kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("Kullanıcı adınızı hatalı girdiniz!")
        hak -= 1
    elif(kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("Parolanızı hatalı girdiniz!")
        hak -= 1
    elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
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
