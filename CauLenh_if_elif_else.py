# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 19:26:45 2022

@author: Gia Bao

Cau lenh re nhanh if-else
"""
#Tinh chan le
x = int(input("Nhap vao 1 so nguyen X: "))
if x%2==0:
    print("{0} la so chan".format(x))
else:
    print("{0} la so le".format(x))
#Tim gia tri lon nhat trpng 3 phan tu
print("\tTim gia tri lon nhat trong 3 gia tri tren:")
gtr1 = int(input("Nhap vao gia tri thu 1: "))    
gtr2 = int(input("Nhap vao gia tri thu 2: "))
gtr3 = int(input("Nhap vao gia tri thu 3: "))

if (gtr1>gtr2) and (gtr1>gtr3):
    print("{0} la gia tri lon nhat.".format(gtr1))
elif (gtr2>gtr1) and (gtr2>gtr3):
    print("{0} la gia tri lon nhat.".format(gtr2))
else:
    print("{0} la gia tri nho nhat.".format(gtr3))
#Tim gia tri nho nhat trpng 3 phan tu
print("\tTim gia tri lon nhat trong 3 gia tri tren:")
gtr1 = int(input("Nhap vao gia tri thu 1: "))    
gtr2 = int(input("Nhap vao gia tri thu 2: "))
gtr3 = int(input("Nhap vao gia tri thu 3: "))

if (gtr1<gtr2) and (gtr1<gtr3):
    print("{0} la gia tri nho nhat.".format(gtr1))
elif (gtr2<gtr1) and (gtr2<gtr3):
    print("{0} la gia tri nho nhat.".format(gtr2))
else:
    print("{0} la gia tri nho nhat.".format(gtr3))    