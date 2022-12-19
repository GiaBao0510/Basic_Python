# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 19:28:03 2022

@author: DELL
"""

#Cac loai print
print()

print(2002)

print("Hello World")

print("Name: "); print("Gia Bao");

print('Pham','Gia','Bao')

print('Pham','Gia',"Bao",2002)

#Su dung tu khoa "sep" trong cau lenh print

print('Pham','Gia','Bao',sep="+")
print('Pham','Gia','Bao',sep=",")
print('Pham','Gia','Bao',sep="*")
print('Pham','Gia','Bao',sep="-")

"""Su dung tu khoa "end" trong cau lenh print thay vi xuong dong thi 
no se keo cau lenh print tiep theo gan no nhat"""

print("Xin chao: ")
print("Gia Bao")

print("Xin chao: ",end="- ")
print("Gia Bao")

hten = "Gia Bao"
age = 20
#Giong nhu c: printf("Ho ten: %s \nTuoi: %d",hten,tuoi);
print("Ho ten: {0} \nTuoi: {1} ".format(hten,age))