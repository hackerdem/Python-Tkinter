from tkinter import *
import tkinter.filedialog as fd
import os
from tkinter import messagebox as mbox
PROGRAM_NAME="Footprint Editor"
root=Tk()
root.geometry('350x350')
root.title(PROGRAM_NAME)
root.attributes('-alpha',0.8)
file_name=None
def exit_editor(event=None):
    if mbox.askokcancel("Quit?","Really quit?"):
        root.destroy()
def display_about_messagebox(event=None):
    mbox.showinfo(
    "About","{} {}".format(PROGRAM_NAME,"\nSimple text editor\n but one day it will be a Python IDE"))
def display_help_messagebox(event=None):
    mbox.showinfo(
    "Help","Help Book: \nSimple text editor\n but one day it will be a Python IDE",icon='question')
def open_file(event=None):
    input_file_name=fd.askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if input_file_name:
        global file_name
        file_name=input_file_name
        root.title('{}-{}'.format(os.path.basename(file_name),PROGRAM_NAME))
        content_text.delete(1.0,END)
        with open(file_name) as _file:
            content_text.insert(1.0,_file.read())
    on_content_changed()
def save(event=None):
    global file_name
    if not file_name:
        save_as()
    else:
        write_to_file(file_name)
    return "break"
def save_as(event=None):
    input_file_name=fd.asksaveasfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if input_file_name:
        global file_name
        file_name=input_file_name
        write_to_file(file_name)
        root.title('{} - {}'.format(os.path.basename(file_name),PROGRAM_NAME))
    return "break"
def write_to_file(file_name):
    try:
        content=content_text.get(1.0,'end')
        with open(file_name,'w') as the_file:
            the_file.write(content)
    except IOError:
        pass
def new_file(event=None):
    root.title("Untitled")
    global file_name
    file_name=None
    content_text.delete(1.0,END)
def cut():
    content_text.event_generate("<<Cut>>")
    on_content_changed()
    return 'break'
def paste():
    content_text.event_generate("<<Paste>>")
    on_content_changed()
    return 'break'
def copy():
    content_text.event_generate("<<Copy>>")
    on_content_changed()
    return 'break'
def undo():
    content_text.event_generate("<<Undo>>")
    on_content_changed()
    return 'break'
def redo(event=None):
    content_text.event_generate("<<Redo>>")
    on_content_changed()
    return 'break' 
def select_all(event=None):
    content_text.tag_add('sel','1.0','end')
    return "break"
def highlight_line(interval=100):
    content_text.tag_remove("active_line",1.0,"end")
    content_text.tag_add("active_line","insert linestart","insert lineend+1c")
    content_text.after(interval,toggle_highlight)
def undo_highlight():
    content_text.tag_remove("active_line",1.0,"end")
def toggle_highlight(event=None):
    if to_highlight_line.get():
        highlight_line()
    else:
        undo_highlight()
    
def get_line_numbers(evet=None):
    output=''
    if show_line_number.get():
        row,col=content_text.index("end").split(".")
        for i in range(1,int(row)):
            output+=str(i)+'\n'
    return output
def update_line_numbers(event=None):
    line_numbers=get_line_numbers()
    line_number_bar.config(state='normal')
    line_number_bar.delete('1.0','end')
    line_number_bar.insert('1.0',line_numbers)
    line_number_bar.config(state='disabled')
    
def on_content_changed(event=None):
    update_line_numbers()
def find_text(event=None):
    search_toplevel=Toplevel(root)
    search_toplevel.title('Find Text')
    search_toplevel.transient(root)
    search_toplevel.resizable(False,False)
    Label(search_toplevel,text="Find All:").grid(row=0,column=0,sticky='e')
    search_entry_widget=Entry(search_toplevel,width=25)
    search_entry_widget.grid(row=0,column=1,padx=2,pady=2,sticky='we')
    search_entry_widget.focus_set()
    ignore_case_value=IntVar()
    Checkbutton(search_toplevel,text='Ignore Case',variable=ignore_case_value).grid(row=1,column=1,sticky='e',padx=2,pady=2)
    Button(search_toplevel,text="Find All",underline=0,command=lambda: search_output(search_entry_widget.get(),ignore_case_value.get(),content_text,search_toplevel,search_entry_widget)).grid(row=0,column=2,sticky='e'+'w',padx=2,pady=2)
    #to delete matched words highlight after using find functionality, we will overwrite close_search_window
    def close_search_window():
        content_text.tag_remove('match','1.0',END)
        search_toplevel.destroy()
    search_toplevel.protocol('WM_DELETE_WINDOW',close_search_window)
    return "break"
def search_output(needle,if_ignore_case,content_text,search_toplevel,search_box):
    content_text.tag_remove('match','1.0',END)
    matches_found=0
    if needle:
        start_pos='1.0'
        while True:
            start_pos=content_text.search(needle,start_pos,nocase=if_ignore_case,stopindex=END)
            if not start_pos:
                break
            end_pos='{}+{}c'.format(start_pos,len(needle))
            content_text.tag_add('match',start_pos,end_pos)
            matches_found+=1
            start_pos=end_pos
        content_text.tag_config('match',foreground='red',background='yellow')
    search_box.focus_set()
    search_toplevel.title('{} matches found'.format(matches_found))


#icons

new_file_icon=PhotoImage(file='icons/new_file.gif')
saveas_file_icon=PhotoImage(file='icons/save.gif')
save_icon=PhotoImage(file='icons/save.gif')
open_file_icon=PhotoImage(file='icons/open_file.gif')
undo_icon=PhotoImage(file='icons/undo.gif')
redo_icon=PhotoImage(file='icons/redo.gif')
cut_icon=PhotoImage(file='icons/cut.gif')
copy_icon=PhotoImage(file='icons/copy.gif')
paste_icon=PhotoImage(file='icons/paste.gif')
find_icon=PhotoImage(file='icons/find_text.gif')
about_icon=PhotoImage(file='icons/about.gif')
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
file_menu.add_command(label='New',accelerator='Ctrl+N',command=new_file,compound='left',image=new_file_icon,underline=0)
file_menu.add_command(label='Open',accelerator='Ctrl+O',command=open_file,compound='left',image=open_file_icon,underline=0)
file_menu.add_command(label='Save',accelerator='Ctrl+S',command=save,compound='left',image=save_icon,underline=0)
file_menu.add_command(label='Save as',accelerator='Shift+Ctrl+S',command=save_as,compound='left',image=saveas_file_icon,underline=0)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=exit_editor,accelerator='Alt+F4')
menu_bar.add_cascade(label='File',menu=file_menu)

#edit menu
edit_menu=Menu(menu_bar,tearoff=0)
edit_menu.add_command(label='Undo',accelerator='Ctrl+Z',command=undo,compound='left',image=undo_icon,underline=0)
edit_menu.add_command(label='Redo',accelerator='Ctrl+Y',command=redo,compound='left',image=redo_icon,underline=0)
edit_menu.add_separator()
edit_menu.add_command(label='Cut',accelerator='Ctrl+X',command=cut,compound='left',image=cut_icon,underline=0)
edit_menu.add_command(label='Copy',accelerator='Ctrl+C',command=copy,compound='left',image=copy_icon,underline=0)
edit_menu.add_command(label='Paste',accelerator='Ctrl+V',command=paste,compound='left',image=paste_icon,underline=0)
edit_menu.add_separator()
edit_menu.add_command(label='Find',accelerator='Ctrl+F',command=find_text,compound='left',image=find_icon,underline=0)
file_menu.add_separator()
edit_menu.add_command(label='Select All',accelerator='Ctrl+A',command=select_all,compound='left',image='',underline=7)
menu_bar.add_cascade(label='Edit',menu=edit_menu)

#view menu
view_menu=Menu(menu_bar,tearoff=0)
show_line_number=IntVar()
show_line_number.set(1)
view_menu.add_checkbutton(label="Show Line Number",variable=show_line_number)
show_cursor_info=IntVar()
show_cursor_info.set(1)
view_menu.add_checkbutton(label="Show Cursor Location at Bottom",variable=show_cursor_info)
to_highlight_line=IntVar()
view_menu.add_checkbutton(label="Highlight Current Line",command=toggle_highlight,onvalue=1,offvalue=0,variable=to_highlight_line)
themes_menu=Menu(menu_bar,tearoff=0)
view_menu.add_cascade(label="Themes",menu=themes_menu)
theme_choice=StringVar()
theme_choice.set('Default')
for i in sorted(color_shemes):
    themes_menu.add_radiobutton(label=i,variable=theme_choice)

menu_bar.add_cascade(label='View',menu=view_menu)

#about menu
about_menu=Menu(menu_bar,tearoff=0)
about_menu.add_command(label='About',command=display_about_messagebox,compound='left',image=about_icon,underline=0)
about_menu.add_command(label='Help',command=display_help_messagebox,compound='left',image='',underline=0)
menu_bar.add_cascade(label='About',menu=about_menu)
root.config(menu=menu_bar)
root.protocol('WM_DELETE_WINDOW',exit_editor)
#shortcut bar
shortcut_bar=Frame(root,height=25,background='#DCDCDC')
shortcut_bar.pack(expand='no',fill='x')

# line number bar
line_number_bar=Text(root,width=4,padx=3,takefocus=0,border=0,background='#778899',state='disabled',wrap='none')
line_number_bar.pack(side='left',fill='y')

#shortcut menu
icons=('new_file','open_file','save','cut','copy','paste','undo','redo','find_text')
for i,icon in enumerate(icons):
    tool_bar_icon=PhotoImage(file='icons/{}.gif'.format(icon))
    cmd=eval(icon)
    tool_bar=Button(shortcut_bar,image=tool_bar_icon,command=cmd)
    tool_bar.image=tool_bar_icon
    tool_bar.pack(side='left')

#text and scroolbar widgets for root window
content_text=Text(root,wrap='word',undo=1,background='#778899',font=("Helvetica", 16),fg="#FFFFFF")
content_text.tag_configure('active_line',background='#000000')
content_text.bind('<Control-y>',redo)# event binding for providing redo functionality
content_text.bind('<Control-Y>',redo) # redo has different conditions in tkinter so we need to do thid in this way
content_text.bind('<Control-a>',select_all)
content_text.bind('<Control-A>',select_all)
content_text.bind('<Control-f>',find_text)
content_text.bind('<Control-F>',find_text)
content_text.bind('<Control-N>', new_file)
content_text.bind('<Control-n>', new_file)
content_text.bind('<Control-O>', open_file)
content_text.bind('<Control-o>', open_file)
content_text.bind('<Control-S>', save)
content_text.bind('<Control-s>', save)
content_text.bind('<KeyPress-F1>',display_help_messagebox)
content_text.bind('<Any-KeyPress>',on_content_changed)
content_text.pack(expand='yes',fill='both')
scroll_bar=Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right',fill='y')

root.mainloop()