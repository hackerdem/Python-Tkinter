from tkinter import *
PROGRAM_NAME="Footprint Editor"

root=Tk()
root.geometry('350x350')
root.title(PROGRAM_NAME)
#icons
#WARNINIG##########change ico is not working make it gif
"""new_file_icon=PhotoImage(file='if_file_173011.ico')
saveas_file_icon=PhotoImage(file='if_Save-as_85541.ico')
save_icon=PhotoImage(file='if_save_173091.ico')
open_file_icon=PhotoImage(file='if_folder-open_173017.ico')"""

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

#edit menu
edit_menu=Menu(menu_bar,tearoff=0)
edit_menu.add_command(label='Undo',accelerator='Ctrl+Z',compound='left',image='',underline=0)
edit_menu.add_command(label='Redo',accelerator='Ctrl+Y',compound='left',image='',underline=0)
edit_menu.add_separator()
edit_menu.add_command(label='Cut',accelerator='Ctrl+X',compound='left',image='',underline=0)
edit_menu.add_command(label='Copy',accelerator='Ctrl+C',compound='left',image='',underline=0)
edit_menu.add_command(label='Paste',accelerator='Ctrl+V',compound='left',image='',underline=0)
edit_menu.add_separator()
edit_menu.add_command(label='Find',accelerator='Ctrl+F',compound='left',image='',underline=0)
file_menu.add_separator()
edit_menu.add_command(label='Select All',accelerator='Ctrl+A',compound='left',image='',underline=0)
menu_bar.add_cascade(label='Edit',menu=edit_menu)
view_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='View',menu=view_menu)

#about menu
about_menu=Menu(menu_bar,tearoff=0)
about_menu.add_command(label='About',compound='left',underline=0)
about_menu.add_command(label='Help',compound='left',image='',underline=0)
menu_bar.add_cascade(label='About',menu=about_menu)
root.config(menu=menu_bar)

#shortcut bar
shortcut_bar=Frame(root,height=25,background='grey')
shortcut_bar.pack(expand='no',fill='x')

# line number bar
line_number_bar=Text(root,width=4,padx=3,takefocus=0,border=0,background='blue',state='disabled',wrap='none')
line_number_bar.pack(side='left',fill='y')

root.mainloop()