# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 16:10:18 2022

@author: Gia Bao

Bai hoc: Cac phep toan so hoc co ban trong python

    Phep toan   Giai thich                      EX:
        +           cong                        x+y
        -           tru                         x-y
        *           nhan                        x-y
        /           chia                        x/y
        %           chia lay phan du            x%y
        **          mu                          x**y
        //          Chia lay phan nguyen        x//y
"""
#Nhung gi ma chung ta nhap tu ban phim thi he thong se mac dinh no la kieu String
#Nhap
a = input("Nhap vao so A: ")
print("Kieu du lieu cua A: ",type(a))
a = float(a)
print("Kieu du lieu cua A: ",type(a))
b = input("Nhap vao so B: ")
print("Kieu du lieu cua B: ",type(b))
b = float(b)
print("Kieu du lieu cua A: ",type(a))
#Xuat
print("{0} + {1} = {2}".format(a, b,a+b))
print("{0} - {1} = {2}".format(a, b,a-b))
print("{0} * {1} = {2}".format(a, b,a*b))
print("{0} / {1} = {2}".format(a, b,a/b))
print("{0} % {1} = {2}".format(a, b,a%b))
print("{0} ** {1} = {2}".format(a, b,a**b))
print("{0} // {1} = {2}".format(a, b,a//b))