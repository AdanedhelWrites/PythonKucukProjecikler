import time

for i in range(1,11):
    print("-----------------------------")
    print("Hesaplanıyor...")
    print("-----------------------------")
    for j in range(1,11):
        time.sleep(0.25)
        print("{} x {} = {}".format(i,j,i*j))