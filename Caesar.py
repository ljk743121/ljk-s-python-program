'''
from tkinter import *

run = Tk()
run.title("Caesar Cipher")
run.geometry('1068x681')
text_l = Text(run,width=67, height=35)  #原始数据录入框
text_l.grid(row=1, column=0, rowspan=10, columnspan=10)
text_r = Text(run,width=70, height=49)  #处理结果展示
text_r.grid(row=1, column=12, rowspan=15, columnspan=10)
text_k = Text(run,width=66, height=9)  # 日志框
text_k.grid(row=13, column=0, columnspan=10)
MODE = ["Caesar Cipher","Nome"]
variable = StringVar()
variable.set(MODE[0])
Button = OptionMenu(master=run,variable=variable,*MODE)
Button.pack()
run.mainloop()
'''
import pystrich
photo = pystrich.EAN13Encoder('690123456789')
