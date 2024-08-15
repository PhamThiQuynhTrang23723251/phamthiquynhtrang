# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:15:19 2024

@author: phamthiquynhtrang
"""
a=float(input("nhap so a:"))
b=float(input("nhap so b:"))
c=float(input("nhap so c:"))
D=b*b-4*a*c
if D==0:
    print("PT có nghiệm kép x1 = x2 =",-b/(2*a))
if D>0:
    print("PT có hai nghiệm x1=",(-b+D**0.5)/(2*a),"và x2=",(-b-D**0.5)/(2*a))
if D<0:
    print("PT vô nghiệm")
