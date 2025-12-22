while True:
    w=float(input(" Nhap chieu dai "))
    h=float(input(" Nhap chieu rong "))   
    if 0.0<=w and h<=100.0:
                  dt=(w*h)
                  cv=(w+h)*2
    break
print( f" chu vi hinh chu nhat:{cv:9.1f}")
print( f" dien tich hinh chu nhat:{dt:9.1f}")
    


    