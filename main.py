import tkinter as Tkinter
import pypinyin

top = Tkinter.Tk()
input = Tkinter.Entry(top)
def jiami():
  print(pypinyin.pinyin(input.get()))
  input.select_clear()
jm = Tkinter.Button(top,text="加密",command=jiami)
jm.pack()
input.pack()
top.mainloop()
