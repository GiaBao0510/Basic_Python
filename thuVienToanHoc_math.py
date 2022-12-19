
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:56:01 2022

@author: Gia Bao
Gioi thieu ve thu vien toan math
"""
import math
#Nhap
x = float(input('Nhap vao 1 so thuc X: '))
y = float(input('Nhap vao 1 so thuc Y: '))
#In
print("PI= {0}".format(math.pi))
print("e= {0}".format(math.e))
print("Tra ve gia tri tran cua {0} .So nguyen nho nhat lon hon hoac bang {1}:  {2}".format(x, x, math.ceil(x)))
print("|{0}| = {1}".format(x, math.fabs(x)))
print("Tra ve gia tri san cua {0} . So nguyen lon nhat nho hon hoac bang {1}: {2}".format(x, x,math.floor(x)))
print("Tra ve e luy thua {0}: e^{1}: {2}".format(x, x,math.exp(x)))
print("Tra ve logarit tu nhieu cua {0} voi co so la e: log e {1} = {2}".format(x, x,math.log(x)))
print("{0}^{1} = {2}".format(x, y,x**y))
print("{0}^{1} = {2}".format(x, y,math.pow(x,y)))
print("sqrt({0}) = {1}".format(x, math.sqrt(x)))