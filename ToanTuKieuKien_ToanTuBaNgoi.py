# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:34:47 2022

@author: GiaBao
Toan tu dieu kien
"""
print("\t\tToan tu dieu kien - Toan tu ba ngoi")
print("\nCu phap: [Tra ve ket qua ban dau neu dieu kien dung] if[kiem tra dieu kien] else[Tra ve ket qua khac neu dieu kien sai]\n")
 
x = int(input("Nhap vao 1 so nguyen X: "))
y = int(input("Nhap vao 1 so nguyen Y: "))

kq1 = "{0} > {1} la: TRUE.".format(x,y) if(x>y) else "{0} > {1} la: FALSE.".format(x,y)

print(kq1)

kq2 = "{0} la so Nguyen Duong".format(x) if(x>0) else  "{0} la so Nguyen Am".format(x)

print(kq2)

kq3 = "{0} la so chan".format(x) if(x%2==0) else "{0} la so le".format(x) 

print(kq3)