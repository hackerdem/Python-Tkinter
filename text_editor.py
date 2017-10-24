from tkinter import *
def cut():
    content_text.event_generate("<<Cut>>")
    return 'break'
def undo():
    content_text.event_generate("<<Undo>>")
    return 'break'
def redo(event=None):
    content_text.event_generate("<<Redo>>")
    return 'break' 
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

""" Color options are listed in a dictionary"""
color_shemes={
    'Default': '#000000.#FFFFFF',
    'Greygarious': '#83406A.#D1D4D1',
    'Aquamarine': '#5B8340.#D1E7E0',
    'Bold Beige': '#4B4620.#FFF0E1',
    'Cobalt Blue': '#ffffBB.#3333aa',
    'Olive Green': '#D1E7E0.#5B8340',
    'Night Mode': '#FFFFFF.#000000',
    }

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
edit_menu.add_command(label='Undo',accelerator='Ctrl+Z',command=undo,compound='left',image='',underline=0)
edit_menu.add_command(label='Redo',accelerator='Ctrl+Y',command=redo,compound='left',image='',underline=0)
edit_menu.add_separator()
edit_menu.add_command(label='Cut',accelerator='Ctrl+X',command=cut,compound='left',image='',underline=0)
edit_menu.add_command(label='Copy',accelerator='Ctrl+C',compound='left',image='',underline=0)
edit_menu.add_command(label='Paste',accelerator='Ctrl+V',compound='left',image='',underline=0)
edit_menu.add_separator()
edit_menu.add_command(label='Find',accelerator='Ctrl+F',compound='left',image='',underline=0)
file_menu.add_separator()
edit_menu.add_command(label='Select All',accelerator='Ctrl+A',compound='left',image='',underline=0)
menu_bar.add_cascade(label='Edit',menu=edit_menu)

#view menu
view_menu=Menu(menu_bar,tearoff=0)
show_line_number=IntVar()
show_line_number.set(1)
view_menu.add_checkbutton(label="Show Line Number",variable=show_line_number)
show_cursor_info=IntVar()
show_cursor_info.set(1)
view_menu.add_checkbutton(label="Show Cursor Location at Bottom",variable=show_cursor_info)
highlight_line=IntVar()
view_menu.add_checkbutton(label="Highlight Current Line",onvalue=1,offvalue=0,variable=highlight_line)
themes_menu=Menu(menu_bar,tearoff=0)
view_menu.add_cascade(label="Themes",menu=themes_menu)
theme_choice=StringVar()
theme_choice.set('Default')
for i in sorted(color_shemes):
    themes_menu.add_radiobutton(label=i,variable=theme_choice)

menu_bar.add_cascade(label='View',menu=view_menu)

#about menu
about_menu=Menu(menu_bar,tearoff=0)
about_menu.add_command(label='About',compound='left',underline=0)
about_menu.add_command(label='Help',compound='left',image='',underline=0)
menu_bar.add_cascade(label='About',menu=about_menu)
root.config(menu=menu_bar)

#shortcut bar
shortcut_bar=Frame(root,height=25,background='#DCDCDC')
shortcut_bar.pack(expand='no',fill='x')

# line number bar
line_number_bar=Text(root,width=4,padx=3,takefocus=0,border=0,background='#778899',state='disabled',wrap='none')
line_number_bar.pack(side='left',fill='y')

#text and scroolbar widgets for root window
content_text=Text(root,wrap='word',undo=1,background='#778899')
content_text.bind('<Control-y>',redo)# event binding for providing redo functionality
content_text.bind('<Control-Y>',redo) # redo has different conditions in tkinter so we need to do thid in this way
content_text.pack(expand='yes',fill='both')
scroll_bar=Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right',fill='y')

root.mainloop()