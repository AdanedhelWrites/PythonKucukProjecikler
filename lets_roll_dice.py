import random
def zar_at(rolls):
    for i in range(0,rolls):
        zar = random.randint(1,6)
    
        print(zar)



def Secim():
    
    while True:
        print("Çıkmak için: '0' -- 1 zar atmak için: '1' -- İki zar atmak için: '2' -- 2'den fazla zar atmak için: '3' tuşlayınız! ")
        secim = int(input("Secimi yapınız:"))
        if secim == 0:
            print("Güle güle !")
            break
        elif secim == 1:
            zar_at(1)
        elif secim == 2:
            zar_at(2)
        elif secim == 3:
            rolls = int(input("Kaç tane zar atıcaksınız?:"))
            zar_at(rolls)
        else:
            print("Böyle bir seçim yapamazsınn")
            
Secim()