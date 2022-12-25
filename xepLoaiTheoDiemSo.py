# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 19:39:47 2022

@author: DELL
"""
print("Xep loai theo diem so:")
diem = float(input("Nhap diem can xet loai: "))
if(diem >= 9):
    print("Loai Xuat Sac")
elif(diem<9 and diem>=8):
    print("Loai gioi")
elif(diem<8 and diem>=7):
    print("Loai kha")
elif(diem<7 and diem>=4):
    print("Loai trung binh")
else:
    print("Loai yeu")