from tkinter import *
PROGRAM_NAME="Footprint Editor"

root=Tk()
root.geometry('350x350')
root.title(PROGRAM_NAME)
#menu bar
menu_bar=Menu(root)
#file menu
file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label='New',accelerator='Ctrl+N',compound='left',image='',underline=0)
file_menu.add_command(label='Open',accelerator='Ctrl+O',compound='left',image='',underline=0)
file_menu.add_command(label='Save',accelerator='Ctrl+S',compound='left',image='',underline=0)
file_menu.add_command(label='Save as',accelerator='Shift+Ctrl+S',compound='left',image='',underline=0)
file_menu.add_separator()
file_menu.add_command(label='Exit',accelerator='Alt+F4')
menu_bar.add_cascade(label='File',menu=file_menu)
edit_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Edit',menu=edit_menu)
view_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='View',menu=view_menu)
about_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='About',menu=about_menu)
root.config(menu=menu_bar)


root.mainloop()