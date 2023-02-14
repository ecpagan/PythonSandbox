import tkinter


class LayoutEnum:
    pack = 'pack'
    place = 'place'
    grid = 'grid'


actual_layout = LayoutEnum.grid


def button_clicked():
    print('Button Clicked')
    new_text = input.get()
    my_label.config(text=new_text)

# Tkinter have a lot of Layout Managers, that define how to position each of the widgets in the GUI.
# There are 3 that you should know about:
# pack: pack each of the widgets next to each other in a vaguely logical format.
#       By default, will always start from the top and then pack every other widget just below the previous one.
# place: is all about precise positioning, so when you place something you can provide X and Y values. Downside is that
# is so specific
# grid: simple concept, imagine the entire program is a grid and you can divide it in any number of columns and rows.
#
# You can't mix up grid and pack in the same program


# Creating a new window and configurations
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # to add padding around the window

# Labels
my_label = tkinter.Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.config(text='New text')
# one of the layouts must be used to place it on the screen
if actual_layout == LayoutEnum.pack:
    my_label.pack()
elif actual_layout == LayoutEnum.place:
    my_label.place(x=0, y=0)
elif actual_layout == LayoutEnum.grid:
    my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)  # to add padding around the widget

# Buttons
# calls function when pressed
button = tkinter.Button(text='Click Me', command=button_clicked)
if actual_layout == LayoutEnum.pack:
    button.pack()
elif actual_layout == LayoutEnum.place:
    button.place(x=100, y=100)
elif actual_layout == LayoutEnum.grid:
    button.grid(column=1, row=1)

# New Button
button2 = tkinter.Button(text='Click Me2', command=button_clicked)
if actual_layout == LayoutEnum.pack:
    button2.pack()
elif actual_layout == LayoutEnum.place:
    button2.place(x=100, y=100)
elif actual_layout == LayoutEnum.grid:
    button2.grid(column=3, row=0)

# Entries
entry = tkinter.Entry(width=10)
# Gets text in entry
print(entry.get())
if actual_layout == LayoutEnum.pack:
    entry.pack()
elif actual_layout == LayoutEnum.place:
    button.place(x=100, y=100)
elif actual_layout == LayoutEnum.grid:
    entry.grid(column=4, row=3)

window.mainloop()  # should be at the very end of the script, to hold the GUI
