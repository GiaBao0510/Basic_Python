# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 19:45:36 2022

@author: DELL
"""
#them goi math
import math
print("\n\t\t\tGiai phuong trinh bac hai:\n")
#nhap
a = float(input("Nhap vao 1 gia tri A: "))
b = float(input("Nhap vao 1 gia tri B: "))
c = float(input("Nhap vao 1 gia tri C: "))
#So sanh dieu kien
delta = b**2 - (4*a*c)
if(a != 0):
    print("\n\tPTB 2:\n")
    if (delta < 0):
        print("Phuong trinh vo nghiem.")
    elif (delta == 0):
        print("Phuong trinh co nghiem kep: X1 = X2 = {0}".format( (-b/2*a)) )
    else:
        print("Phuog trinh co hai nghiem phan biet:\nX1 = {0} \nX2 = {1}".format( (-b-math.sqrt(delta))/(2*a) , (-b+math.sqrt(delta))/(2*a)) )
else:
    print("\n\tPTB 1:\n")
    if b == 0:
        if c == 0:
            print("Phuong trinh vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        print("Phuong trinh co nghiem duy nhat: {0}".format( -c/b))
        