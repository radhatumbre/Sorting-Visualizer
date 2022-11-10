# importing tkinter gui
import random
from tkinter import *
from tkinter import ttk
from tkinter import font
import time

# Creating bars
barList = []
bar_size = []
lengthList = []

def generate_arr():
    barList.clear()
    bar_size.clear()
    lengthList.clear()
    # Clearing the canvas
    canvas.delete('all')
    n = int(arr_size.get())
    width_bar = width*0.96 / n - 5
    xstart = width*0.02
    for i in range(n):
        xend = width_bar + xstart
        randomY = random.randint(30, 600)
        bar_size.append(randomY)
        bar = canvas.create_rectangle(xstart, randomY, xend, 0, fill="#606C38")
        barList.append(bar)
        xstart += width_bar + 5
        xend += width_bar


def sort_speed():
    val = selected_speed.get()
    if val == 'Slow':
        speed = 0.1
    elif val == 'Medium':
        speed = 0.05
    elif val == 'Fast':
        speed = 0
    return speed

def swap_two_pos(pos_0, pos_1):
    x_00, _, x_01, _ = canvas.coords(pos_0)
    x_10, _, x_11, _ = canvas.coords(pos_1)
    canvas.move(pos_0, x_10 - x_00, 0)
    canvas.move(pos_1, x_01 - x_11, 0)


def bubble_sort():
    speed = sort_speed()
    for i in range(0, len(bar_size) - 1):
        for j in range(len(bar_size) - 1 - i):

            canvas.itemconfig(barList[j], fill='#65a765')
            canvas.itemconfig(barList[j + 1], fill='#65a765')  #283618
            if (bar_size[j] > bar_size[j + 1]):
                pos_0 = barList[j]
                pos_1 = barList[j + 1]
                temp = bar_size[j + 1]
                bar_size[j + 1] = bar_size[j]
                bar_size[j] = temp
                swap_two_pos(pos_0, pos_1)
                # canvas.create_rectangle(pos_0, fill='red')
                # canvas.create_rectangle(pos_1, fill='red')
                barList[j], barList[j + 1] = barList[j + 1], barList[j]
            # canvas.itemconfig(barList[j], fill='blue')
            # canvas.itemconfig(barList[j + 1], fill='blue')
            root.update()
            time.sleep(speed)
            canvas.itemconfig(barList[j], fill='#606C38')
            canvas.itemconfig(barList[j + 1], fill='#606C38')


def insertion_sort():
    # Outer loop to traverse through 1 to len(list1)
    for i in range(1, len(bar_size)):

        value = bar_size[i]
        temp = barList[i]
        # Move elements of list1[0..i-1], that are
        # greater than value, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and value < bar_size[j]:
            bar_size[j + 1] = bar_size[j]

            pos_0 = barList[j]
            pos_1 = barList[j + 1]

            x1s,y1,x1e,y1pos = canvas.coords(pos_0)
            x2s,y2,x2e,y2pos  = canvas.coords(pos_1)
            canvas.move(pos_1,x1s,y1,x1e,y1pos)

            j -= 1
        bar_size[j + 1] = value
        barList[j + 1] = temp




# delete if necessary
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master


# initialize tkinter
root = Tk()
app = Window(root)  # delete if necessary

# getting screen width and height of display
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# setting tkinter window size
root.geometry("%dx%d" % (width, height))
root.title("Sorting Visualizer")
fonts=list(font.families())

# Navigation Bar
nav = Canvas(root, width=width, height=100, bg='#BC6C25')
nav.pack()
canvas = Canvas(root, width=width, height=height, bg='#FEFAE0')
canvas.place(x=0, y=100)
# fullbg.create_rectangle(30,50,100,0,fill="#606C38")
# fullbg.create_rectangle(105,50,200,0,fill="#283618")
# fullbg.create_rectangle(300,500,200,0,fill="#283618")

# slider
# label for the slider
slider_label = Label(nav, text='Array Size :', font=("Arial", 20), height=2, width=10, fg='black',
                     bg='#BC6C25')  # background should be same as canvas
slider_label.pack()
nav.create_window(850, 50, window=slider_label)

arr_size = StringVar()  # string variable
sb = Spinbox(root, textvariable=arr_size, width=5, from_=20, to=100)
nav.create_window(950, 52, window=sb)


speed_label = Label(nav, text='Speed :', font=("Arial", 20), height=2, width=10, fg='black',
                     bg='#BC6C25')  # background should be same as canvas
speed_label.pack()

nav.create_window(1050, 50, window=speed_label)

selected_speed = StringVar()
speed_choosen = ttk.Combobox(root, width=10, textvariable=selected_speed)
speed_choosen['values'] = ('Slow', 'Medium', 'Fast')
speed_choosen.set( "Fast" )
nav.create_window(1150, 52, window=speed_choosen)
speed_choosen.current()


title_label = Label(nav, text='Sorting Visualizer', font=(fonts[102], 40), height=1, width=20, fg='black',
                     bg='#BC6C25')  # background should be same as canvas
title_label.pack()
nav.create_window(250, 50, window=title_label)



# Creating a Button
btn_arr_generate = Button(root, text='Generate New Array', bg='#DDA15E', height=2, width=20, command=generate_arr)
btn_sort = Button(root, text='Sort', bg='#DDA15E', height=2, width=10, command=bubble_sort)

# Set the position of button to coordinate (100, 20)
btn_arr_generate.place(x=530, y=30)
btn_sort.place(x=1250, y=30)

root.mainloop()




