# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:36:29 2024

@author: phamthiquynhtrang
"""
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a==b==c:
    print("Đây là tam giác đều")
elif a==b or a==c or b==c:
    print("Đây là tam giác cân")
    if a**2 + b**2== c**2 or b**2 + c**2== b**2 or a**2 + c**2== b**2:
        print("Đây là tam giác vuông cân")
elif a**2 + b**2== c**2 or b**2 + c**2== b**2 or a**2 + c**2== b**2:
    print("Đây là tam giác vuông")
else:
        print("Đây là tam giác thường")
    
           
    
            
    
    

    
   
    
   
    
   
    
   
    
   
    
   
    
        
   
   