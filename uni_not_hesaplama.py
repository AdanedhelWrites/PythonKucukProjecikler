import time

vize = int(input("Öğrencinin vize notu :"))
final = int(input("Öğrencinin final notu :"))

h = vize * 0.40 + final * 0.60
print("Öğrencinin notu hesaplanıyor..")
time.sleep(1.5)

if h >= 88 and h <= 100:
    print("Öğrencinin harf notu: AA \nÖğrenci Başarıyla dersi geçti...")
elif h >= 81 and h < 88:
    print("Öğrencinin harf notu BA \nÖğrenci Başarıyla dersi geçti...")
elif h >= 75 and h < 81:
    print("Öğrencinin harf notu BB \nÖğrenci Başarıyla dersi geçti...")
elif h >= 66 and h < 75:
    print("Öğrencinin harf notu CB \nÖğrenci Başarıyla dersi geçti...")
elif h >= 60 and h < 66:
    print("Öğrencinin harf notu CC \nÖğrenci Başarıyla dersi geçti...")
elif h >= 55 and h < 60:
    print("Öğrencinin harf notu DC \nÖğrenci dersi geçemedi !!")
elif h >= 48 and h < 55:
    print("Öğrencinin harf notu DD \nÖğrenci dersi geçemedi !!")
elif h >= 0 and h < 48:
    print("Öğrencinin harf notu FD \nÖğrenci dersi geçemedi !!")
elif h > 100 or vize > 100 or final > 100:
    print("Girilen not bu kadar büyük olamaz !!")
    
else:
    print("Öğrencinin harf notu FF \nÖğrenci devamsızlıktan kalmıştır !!!!")