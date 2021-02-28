x = 1
y = 1
fibo = [x,y]
for i in range(20):
    x,y = y,x+y
    fibo.append(y)
print(fibo)    