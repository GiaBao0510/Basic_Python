# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 15:53:51 2022

@author: GIa Bao

List: la 1 chuoi cac muc co thu tu> No la mot kieu du lieu duoc su dung nhieu nhat trong python
va rat linh hoat. Tat ca cac muc trong danh sach khong phai cung loai

"""

#Tao ra 1 list rong
emtyList = []

#Tao ra 1 doi tuong list
emptyList2 = list()

print(emtyList)
print(emptyList2)

#tao ra danh sach co du lieu
colors = ["red","blue","green","black","yellow","orange","white","brown"]

#Lay tat ca gia tri trong list
print(colors)
print(colors[:])
#Lay gia tri tai vi tri nao do trong list
print(colors[6])
#Lay cac phan tu dua tren chi so xuat phat va chi so ket thuc
print(colors[2:5])
""" so phuong thuc cua kieu list""" 
#1.Phuong thuc append("values") dung de day 1 phan tu vao cuoi danh sach
colors.append("pink")
print(colors)
#2.Phuong thuc insert(index,value) dung them them 1 phan tu mang gia tri nao do vao vi tri ma minh mong muon
colors.insert(5,"violet")
print(colors[:])
#3.len(object) phuong thuc nay dung de lay so luong phan tu cua doi tuong nao do
print('So luong trong danh sach colors: ',len(colors))

    #VD them phan thu vao cuoi danh sach
colors[len(colors):] = ["grey"]
colors[len(colors):] = ['silver']
print(colors)

#4.count() phuong nay dung de dem so phan tu thoa dieu kien
print("So mau den: ",colors.count("black"))
print('so mau do: ',colors.count("red"))
#5.remove(value) Xoa phan tu dua tren gia tri
colors.remove("silver")
print(colors[:])
print('So luong trong danh sach colors: ',len(colors))
colors.remove('white')
print(colors[:])
print('So luong trong danh sach colors: ',len(colors))
    #Vd xoa phan tu dua tren gia tri theo dieu kien
if "blue" in colors:
       colors.remove("blue")
       print(colors[:])
       print('So luong trong danh sach colors: ',len(colors))
#6.pop()Phuong thuc nay xoa phan tu ra khoi danh sach dua tren vi tri
colors.pop(0)
print(colors[:])
print('So luong trong danh sach colors: ',len(colors))
#7.reverse() phuong thuc nay dung de dao nguoc danh sach
print('Danh sach lu dau')
print(colors[:])
print('Danh sach sau khi bi dao nguoc:')
colors.reverse()
print(colors[:])
#8. sort() phuong thuc nay dung de sap xep danh sach theo thu tu
colors.sort()
print(colors)
    #Neu danh sach la so
print("Sap xep danh sach so:")
number = list()
number.append(6)
number[len(number):] = [2,5,7,8,0,9,1,4,3]
number.sort()
print(number)
    #Sap xep giam dan
print("\tSap xep giam dan")
colors.sort(reverse = True)
print('DAnh sach bang mau sac:')
print(colors)
print('DAnh sach bang phan tu la kieu so:')
number.sort(reverse = True)
print(number)
#clear() Phuong thuc nay dung de xoa sach phan tu ben trong danh sach
print("Xoa sach danh sach colors")
colors.clear()
print(colors)
print('So luong trong danh sach colors: ',len(colors))
print("Xoa sach phan tu trong danh sach number: ")
number.clear()
print(number)
print("So luong phan tu trong danh sach number:",len(number))