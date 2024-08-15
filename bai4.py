# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:04:31 2024

@author: phamthiquynhtrang
"""
s= float(input("nhập số km quãng đường: "))
sotienla = 0
if s<=1:
   sotienla = 20000
elif s<=3:
    sotienla = (s-1)*13000
elif s<=8:
    sotienla = 3*13000+(s-3)*12000
else:
    sotienla = 3*13000+(s-3)*12000+(s-8)*10000
if sotienla > 100000:
    sotienla = (3*13000+(s-3)*12000+(s-8)*10000)*0.92
print("Tổng tiền: ",int(sotienla))
        
        
   
   