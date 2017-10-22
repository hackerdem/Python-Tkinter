from tkinter import *
root=Tk()
root.configure(background='#4d4d4d') #top level styling

root.option_readfile('options.txt')

mytext=Text(root,background='#101010',foreground='#6d6d6d',borderwidth=2,relief='groove')

mytext.insert(END,"Style is knowing who you are,what you want to say")
mytext.grid(row=0,column=0,columnspan=6,padx=5,pady=5)

Button(root,text='*').grid(row=1,column=1)
Button(root,text='^').grid(row=1,column=2)
Button(root,text='#').grid(row=1,column=3)
Button(root,text='<').grid(row=2,column=1)
Button(root,text='OK',cursor='target').grid(row=2,column=2)
Button(root,text='>').grid(row=2,column=3)
Button(root,text='+').grid(row=3,column=1)
Button(root,text='v').grid(row=3,column=2)
Button(root,text='-').grid(row=3,column=3)
for i in range(9):
    Button(root,text=str(i+1)).grid(row=4+i//3,column=1+i%3)
root.mainloop()

