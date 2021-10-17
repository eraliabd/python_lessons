# -*- coding: utf-8 -*-
"""
@Muallif: Erali Abdinazarov 16/11/2021
"""
#WHILE va RO'YXATLAR

#Masala_sharti:
Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

mahsulotlar = []
while True:
    savol = "Mahsulot nomini kiriting: "
    mahsulot = input(savol)
    mahsulotlar.append(mahsulot)
    print(f"{mahsulot.title()}ga buyurtma berildi")
    takror = input("Yana mahsulot olasizmi (ha/yo'q) ")
    if takror != 'ha':
        break
    
print("Buyurtmangiz!")
print(mahsulotlar)
    




























    
