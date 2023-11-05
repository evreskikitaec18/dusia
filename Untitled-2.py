from tkinter import*

def clicked():
    a = txt.get()
    print(a)
    b = txt1.get()
    print(b)

    a = int(a)
    b = int(b)
    if  btn :
        c = a + b
        c = str(c) 
        txt2 = print(c)
        lbl3.configure(text= c)


def clicked1():
    a = txt.get()
    print(a)
    b = txt1.get()
    print(b)

    a = int(a)
    b = int(b)
    if  btn1 :
        c = a - b
        c = str(c) 
        txt2 = print(c)
        lbl3.configure(text= c)

def clicked2():
    a = txt.get()
    print(a)
    b = txt1.get()
    print(b)

    a = int(a)
    b = int(b)
    if  btn2 :
        c = a / b
        c = str(c) 
        txt2 = print(c)
        lbl3.configure(text= c)

def clicked3():
    a = txt.get()
    print(a)
    b = txt1.get()
    print(b)

    a = int(a)
    b = int(b)
    if  btn3 :
        c = a * b
        c = str(c) 
        txt2 = print(c)
        lbl3.configure(text= c)

window = Tk()
window.title("!")
window.geometry('400x250')
lbl0 = Label(window, text= "калькулятор")
lbl0.pack()

lbl1 = Label(window, text= "Первое число ")
lbl1.pack()

txt = Entry (window, width= 10)
txt.pack()

lbl2 = Label(window, text= "Второе число ")
lbl2.pack()

txt1 = Entry (window, width= 10)
txt1.pack()

lbl3 = Label(window, text= " Ответ ")
lbl3.pack()


btn = Button(window, text = " + ", command= clicked )
btn.pack()
btn1 = Button(window, text = " - " , command= clicked1)
btn1.pack()
btn2 = Button(window, text = " / ", command=clicked2)
btn2.pack()
btn3 = Button(window, text = " * ", command=clicked3)
btn3.pack()

window.mainloop()