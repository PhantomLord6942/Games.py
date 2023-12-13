from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Text Editor")


# Functions
def open_file():
    open_file = filedialog.askopenfile(mode='r')
    if open_file:
        content = open_file.read()
        text_area.delete(1.0, END)
        text_area.insert(1.0, content)


def save_file():
    save_file = filedialog.asksaveasfile(mode='w')
    if save_file:
        content = text_area.get(1.0, END)
        save_file.write(content)


# UI Design
text_area = Text(root, width=40, height=10, font=("Helvetica", 16))
text_area.pack(pady=20)

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

# New file function
def new_file():
    text_area.delete(1.0, END)
file_menu.add_command(label="New", command=new_file)

# Format menu
format_menu = Menu(menu_bar, tearoff=0)
format_menu.add_command(label="Font")
format_menu.add_command(label="Color")
menu_bar.add_cascade(label="Format", menu=format_menu)

# Search and replace
def find_text():
    search_top = Toplevel(root)
    search_entry = Entry(search_top)
    search_button = Button(search_top, text="Find")
    replace_entry = Entry(search_top)
    replace_button = Button(search_top, text="Replace")

# Keyboard shortcuts
root.bind('<Control-s>', save_file)
root.bind('<Control-o>', open_file)

# Syntax highlighting
from tkinter import font
text_area.tag_configure('keyword', foreground='blue')
text_area.tag_configure('string', foreground='red')
# Apply tags
# Add this:

# Apply keyword tag
start_index = '1.0'
# ...tag_add code

# Apply string tag
start_index = '1.0'
# ...tag_add code

# Apply keyword tag
start_index = '1.0'
while True:
    start_index = text_area.search('def ', start_index, stopindex=END)
    if not start_index:
        break
    end_index = f'{start_index}+3c'
    text_area.tag_add('keyword', start_index, end_index)
    start_index = end_index

# Apply string tag
start_index = '1.0'
while True:
    start_index = text_area.search('"', start_index, stopindex=END)
    if not start_index:
        break
    end_index = text_area.search('"', start_index + 1, stopindex=END)
    if not end_index:
        break
    text_area.tag_add('string', start_index, end_index)
    start_index = end_index

font_options = ["Arial", "Times", "Courier"]

font_var = StringVar()
font_var.set(font_options[0])

font_menu = OptionMenu(format_menu, font_var, *font_options)
font_menu.config(bg="white")
format_menu.add_cascade(label="Font", menu=font_menu)

def change_font(event=None):
    text_area.config(font=font_var.get())

font_var.trace("w", change_font)

color_options = ["black", "white", "red", "green", "blue"]

color_var = StringVar()
color_var.set(color_options[0])

color_menu = OptionMenu(format_menu, color_var, *color_options)
format_menu.add_cascade(label="Color", menu=color_menu)


def change_color(event=None):
    text_area.config(fg=color_var.get())

color_var.trace("w", change_color)


text_area.config(bg="black", fg="white")

root.mainloop()
