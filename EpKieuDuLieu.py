# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 15:53:26 2022

@author: Gia Bao
Bai hoc: Ep kieu du lieu(Chuyen doi kieu)
Python co 2 cach ep kieu du lieu
"""

"""
    1.Chuyen kieu ngam dinh: Python tu dong chuyen kieu nay sang kieu du lieu khac. Qua trinh 
nay khong co su tham gia cua nguoi dung
"""
A = 10
B = 3.4
C = A/B 
"""Neu co 2 kieu du lieu khac nhau ma gan cho bien nao do thi he thong xem kieu du lieu 
Ben nao lon hon. Tu do bien duoc gan se co kieu du lieu cua bien co kieu du lieu lon nhat trong
2 hoac nhieu bien.
"""
print(C)
print("Kieu du lieu cua A:",type(A))
print("Kieu du lieu cua B:",type(B))
print("Kieu du lieu cua C:",type(C))

# Khong the lay kieu so ma thao tac voi kieu chuoi

"""
    2.Chuyen kieu ro rang: do chung ta chuyen doi kieu du lieu cua mot doi tuong sang thanh
kieu bat buoc. Cu phap: Ten_Kieu_Du_Lieu(Ten bien)
"""
n = 100
m = "300"
print(str(n)+m)
print(n+int(m))