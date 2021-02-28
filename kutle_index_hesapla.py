import time

boy = float(input("Tam boyunu giriniz :"))
kilo= float(input("Tam kilonuzu giriniz :"))

kitlo_index = kilo / (boy**2)
time.sleep(0.5)
print("Hesaplanıyor...")
time.sleep(2)

if (kitlo_index < 18.5):
    print("Çok zayıfsınız !!")
elif(kitlo_index >= 18.5 and kitlo_index < 25):
    print("Normalsiniz formunuzu korumaya devam edin..")
elif(kitlo_index >= 25 and kitlo_index < 30):
    print("Hafif kilolusunuz biraz dikkat ediniz !")
else:
    print("Aşırı kilolusunuz. Sağlığınıza dikkat edin !!!!")