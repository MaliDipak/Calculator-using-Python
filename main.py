# Calculator using Python Tkinter
from tkinter import *


def click(event):
    global scvalue
    txt = event.widget.cget("text")
    if txt == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif txt == 'C':
        scvalue.set('')
        screen.update()
    else:
        scvalue.set(scvalue.get()+txt)
        screen.update()


root = Tk()

scvalue = StringVar()
scvalue.set("")

root.geometry("375x606")
root.iconbitmap("icon.ico")
root.title("Calculator By Dipak C Mali")
root.resizable(0,0)

screen = Entry(root, font='lucida 20 bold', textvariable=scvalue)
screen.pack(fill=X, padx=10, pady=10, ipadx=10, ipady=5)


f1 = Frame(root, bg='grey')
f1.pack()
b1 = Button(f1, text='/', relief=RIDGE, borderwidth=20,
            font='lucida 15 bold', width=5, bg='yellow', fg='red')
b1.pack(anchor='w', padx=5, pady=5, side='left')
b1.bind("<Button-1>", click)
b1 = Button(f1, text='*', relief=RIDGE, borderwidth=20,
            font='lucida 15 bold', width=5, bg='yellow', fg='red')
b1.pack(anchor='w', padx=5, pady=5, side='left')
b1.bind("<Button-1>", click)
b1 = Button(f1, text='C', relief=RIDGE, borderwidth=20,
            font='lucida 15 bold', width=5, bg='yellow', fg='red')
b1.pack(anchor='w', padx=5, pady=5, side='left')
b1.bind("<Button-1>", click)


f1 = Frame(root, bg='grey')
f1.pack()
b1 = Button(f1, text='7', relief=RIDGE, borderwidth=20,
            font='lucida 15 bold', width=5, bg='yellow', fg='red')
b1.pack(anchor='w', padx=5, pady=5, side='left')
b1.bind("<Button-1>", click)
b1 = Button(f1, text='8', relief=RIDGE, borderwidth=20,
            font='lucida 15 bold', width=5, bg='yellow', fg='red')
b1.pack(anchor='w', padx=5, pady=5, side='left')
b1.bind("<Button-1>", click)
b1 = Button(f1, text='9', relief=RIDGE, borderwidth=20,
            font='lucida 15 bold', width=5, bg='yellow', fg='red')
b1.pack(anchor='w', padx=5, pady=5, side='left')
b1.bind("<Button-1>", click)


f1 = Frame(root, bg='grey')
f1.pack()
b1 = Button(f1, text='4', relief=RIDGE, borderwidth=20,
            font='lucida 15 bold', width=5, bg='yellow', fg='red')
b1.pack(anchor='w', padx=5, pady=5, side='left')
b1.bind("<Button-1>", click)
b1 = Button(f1, text='5', relief=RIDGE, borderwidth=20,
            font='lucida 15 bold', width=5, bg='yellow', fg='red')
b1.pack(anchor='w', padx=5, pady=5, side='left')
b1.bind("<Button-1>", click)
b1 = Button(f1, text='6', relief=RIDGE, borderwidth=20,
            font='lucida 15 bold', width=5, bg='yellow', fg='red')
b1.pack(anchor='w', padx=5, pady=5, side='left')
b1.bind("<Button-1>", click)


f1 = Frame(root, bg='grey')
f1.pack()
b1 = Button(f1, text='1', relief=RIDGE, borderwidth=20,
            font='lucida 15 bold', width=5, bg='yellow', fg='red')
b1.pack(anchor='w', padx=5, pady=5, side='left')
b1.bind("<Button-1>", click)
b1 = Button(f1, text='2', relief=RIDGE, borderwidth=20,
            font='lucida 15 bold', width=5, bg='yellow', fg='red')
b1.pack(anchor='w', padx=5, pady=5, side='left')
b1.bind("<Button-1>", click)
b1 = Button(f1, text='3', relief=RIDGE, borderwidth=20,
            font='lucida 15 bold', width=5, bg='yellow', fg='red')
b1.pack(anchor='w', padx=5, pady=5, side='left')
b1.bind("<Button-1>", click)


f1 = Frame(root, bg='grey')
f1.pack()
b1 = Button(f1, text='0', relief=RIDGE, borderwidth=20,
            font='lucida 15 bold', width=5, bg='yellow', fg='red')
b1.pack(anchor='w', padx=5, pady=5, side='left')
b1.bind("<Button-1>", click)
b1 = Button(f1, text='.', relief=RIDGE, borderwidth=20,
            font='lucida 15 bold', width=5, bg='yellow', fg='red')
b1.pack(anchor='w', padx=5, pady=5, side='left')
b1.bind("<Button-1>", click)
b1 = Button(f1, text='-', relief=RIDGE, borderwidth=20,
            font='lucida 15 bold', width=5, bg='yellow', fg='red')
b1.pack(anchor='w', padx=5, pady=5, side='left')
b1.bind("<Button-1>", click)


f1 = Frame(root, bg='grey')
f1.pack()
b1 = Button(f1, text='+', relief=RIDGE, borderwidth=20,
            font='lucida 15 bold', width=5, bg='yellow', fg='red')
b1.pack(anchor='w', padx=5, pady=5, side='left')
b1.bind("<Button-1>", click)
b1 = Button(f1, text='=', relief=RIDGE, borderwidth=20,
            font='lucida 15 bold', width=5, bg='yellow', fg='red')
b1.pack(anchor='w', padx=5, pady=5, side='left')
b1.bind("<Button-1>", click)
b1 = Button(f1, text='%', relief=RIDGE, borderwidth=20,
            font='lucida 15 bold', width=5, bg='yellow', fg='red')
b1.pack(anchor='w', padx=5, pady=5, side='left')
b1.bind("<Button-1>", click)


root.config(bg='grey')

root.mainloop()
