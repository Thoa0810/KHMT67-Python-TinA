def GTLN(m,n,k):
    maxx=m
    if maxx<n:
        maxx=n
    if maxx<k:
        maxx=k
    return maxx
def GTNN(m,n,k):
    minx=m
    if minx>n:
        minx=n
    if minx>k:
        minx=k
    return minx
m=int(input(" Nhap so m:"))
n=int(input("Nhap so n:"))
k=int(input("Nhap so k:"))
max=GTLN(m,n,k)
print(f"So lon nhat la {max}")
min=GTNN(m,n,k)
print(f"So nho nhat la {min}")

    
    
    
    
        
 