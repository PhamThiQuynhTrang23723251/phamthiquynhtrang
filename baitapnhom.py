# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:44:14 2024

@author: phamthiquynhtrang
"""

GPA = float(input("nhap diem trung binh:"))
if GPA < 3.5:
    print("Học lực kém")
elif 3.5 <= GPA <= 5.0:
    print("Học lực yếu")
elif 5.0 <= GPA <= 7.0:
    print("Học lực trung bình")
elif 8.0 <= GPA <=9.0:
    print("Học lực khá")
elif 9.0 <= GPA <= 10:
    print("Học lực xuất sắc")
else:
    print("Không xác định")