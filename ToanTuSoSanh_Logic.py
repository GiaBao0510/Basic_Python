# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:41:56 2022

@author: DELL
"""

        #Phep toan so sanh
#Nhap
print("\t\tSo sanh giua hai bien:")
x = int(input("Nhap vao 1 so nguyen X: "))
y = int(input("Nhap vao 1 so nguyen Y: "))
z = int(input("Nhap vao 1 so nguyen Z: "))
#So sanh i ra ket qua: true or false
print("{0} > {1} ket qua: {2}".format(x, y, x>y))
print("{0} < {1} ket qua: {2}".format(x, y, x<y))
print("{0} >= {1} ket qua: {2}".format(x, y, x>=y))
print("{0} <= {1} ket qua: {2}".format(x, y, x<=y))
print("{0} == {1} ket qua: {2}".format(x, y, x==y))
print("{0} != {1} ket qua: {2}".format(x, y, x!=y))
        #Phep toan logic: and , or , not
print("\n\t\tPhep toan logic:\n")
print("(X:{0} < Y:{1}) and (Z:{2} < Y:{3}) ket qua: {4}".format(x, y,z,y, (x<y)and(z<y) ))
print("(X:{0} < Y:{1}) or (Z:{2} < Y:{3}) ket qua: {4}".format(x, y,z,y, (x<y)or(z<y) ))
print("Not(X:{0} == Y:{1}) ket qua: {2}".format(x, y,not(x == y)))
print("Not(Z:{0} != Y:{1}) ket qua: {2}".format(x, y,not(z != y)))