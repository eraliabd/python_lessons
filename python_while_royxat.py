# -*- coding: utf-8 -*-
"""
@Muallif: Erali Abdinazarov 16/11/2021
"""
#WHILE va RO'YXATLAR


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
    




























    