poz = -1

def ara(liste,n):
    
    lower=0
    upper = len(liste)-1
    
    while lower <= upper:
        mid = (lower+upper) // 2
        
        if liste[mid] == n:
            globals ()["poz"] = mid
            return True
        else:
            if liste[mid] < n:
                lower= mid+1
            else:
                upper = mid-1
    return False
    
    
    
liste = [2,5,8,15,26,78,25,85,90,190,256,554,567,115,656,245]

liste.sort()
n= 567

if ara(liste,n):
    print("Bulundu:",poz+1)
else:
    print("Bulunamadı")
