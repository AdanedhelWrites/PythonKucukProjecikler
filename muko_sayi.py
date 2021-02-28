def mukemmel(sayı):
    toplam = 0
    for i in range(1,sayı):
        if(sayı % i == 0):
            toplam += i
    return toplam == sayı
import time
deger = int(input("Kaça kadar olan sayıya kadar mükemmel sayı hesaplansın..\t Çok büyük değerlerde bekletebilir..:"))
print("Hesaplanıyor..")
time.sleep(3)
for i in range(1,deger):
    if(mukemmel(i)):
        time.sleep(5)
        print("Mükemmel Sayı:")
        print(i)






