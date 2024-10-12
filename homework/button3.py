import tkinter as tk
from tkinter import *

def on_click():
    kg_value = iphone_kg.get()
    thb_value = thb.get()    
    lbs = kg_value * 1.254 
    exchange_value = thb_value * 0.03  
    iphone_lbs.set(f'{lbs:.2f} lbs.')  
    exchange.set(f'{exchange_value:.2f} USD')  

root = Tk()
root.option_add("*Font", "impact 20")
iphone_kg = DoubleVar()
iphone_lbs = StringVar()
thb = DoubleVar()
exchange = StringVar()

Entry(root, textvariable=iphone_kg, width=10, justify="right").pack(side=LEFT, padx=10)
Label(root, text="kg").pack(side=LEFT, padx=10)
Button(root, text=" = ", bg="blue", command=on_click).pack(side=LEFT)
Label(root, textvariable=iphone_lbs).pack(side=LEFT, padx=10)  

Entry(root, textvariable=thb, width=10, justify="right").pack(side=LEFT, padx=50)
Label(root, text="THB").pack(side=LEFT, padx=10)
Button(root, text=" = ", bg="red", command=on_click).pack(side=LEFT)
Label(root, textvariable=exchange, padx=10).pack(side=LEFT)  
root.mainloop()
