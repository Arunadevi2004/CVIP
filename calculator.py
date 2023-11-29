from tkinter import *
root=Tk()
root.title("CALCULATOR")
input=Entry(root,width=50,font=('arial', 12, 'bold'))
input.grid(row=0,column=0,columnspan=4,padx=15,pady=15)
def click(num):
    current=input.get()
    input.delete(0,END)
    input.insert(0,str(current)+str(num))
    return
def add():
    current=input.get()
    global math
    math='addition'
    global fnum
    fnum=int(current)
    input.delete(0,END)
    return
def sub():
    current=input.get()
    global math
    math='subtraction'
    global fnum
    fnum=int(current)
    input.delete(0,END)
    return
def mul():
    current=input.get()
    global math
    math='multiplication'
    global fnum
    fnum=int(current)
    input.delete(0,END)
    return
def div():
    current=input.get()
    global math
    math='division'
    global fnum
    fnum=int(current)
    input.delete(0,END)
    return
def clear():
    input.delete(0,END)
    return
def equal():
    secondnum=input.get()
    input.delete(0,END)
    if math=='addition':
        input.insert(0,fnum+int(secondnum))
    elif math=='subtraction':
        input.insert(0,fnum-int(secondnum))
    elif math=='multiplication':
        input.insert(0,fnum*int(secondnum))
    elif math=='division':
        input.insert(0,fnum/int(secondnum))
    return 
button_1=Button(root,text="1",padx=50,pady=25,font=('arial', 18, 'bold'),command=lambda: click(1))
button_2=Button(root,text="2",padx=50,pady=25,font=('arial', 18, 'bold'),command=lambda: click(2))
button_3=Button(root,text="3",padx=50,pady=25,font=('arial', 18, 'bold'),command=lambda: click(3))
button_4=Button(root,text="4",padx=50,pady=25,font=('arial', 18, 'bold'),command=lambda: click(4))
button_5=Button(root,text="5",padx=50,pady=25,font=('arial', 18, 'bold'),command=lambda: click(5))
button_6=Button(root,text="6",padx=50,pady=25,font=('arial', 18, 'bold'),command=lambda: click(6))
button_7=Button(root,text="7",padx=50,pady=25,font=('arial', 18, 'bold'),command=lambda: click(7))
button_8=Button(root,text="8",padx=50,pady=25,font=('arial', 18, 'bold'),command=lambda: click(8))
button_9=Button(root,text="9",padx=50,pady=25,font=('arial', 18, 'bold'),command=lambda: click(9))
button_0=Button(root,text="0",padx=50,pady=25,font=('arial', 18, 'bold'),command=lambda: click(0))
button_add=Button(root,text="+",padx=50,pady=25,font=('arial', 18, 'bold'),command=add)
button_sub=Button(root,text="-",padx=50,pady=25,font=('arial', 18, 'bold'),command=sub)
button_mul=Button(root,text="x",padx=50,pady=25,font=('arial', 18, 'bold'),command=mul)
button_div=Button(root,text="/",padx=50,pady=25,font=('arial', 18, 'bold'),command=div)
button_clear=Button(root,text="AC",padx=45,pady=25,font=('arial', 18, 'bold'),command=clear)
button_equal=Button(root,text="=",padx=50,pady=25,font=('arial', 18, 'bold'),command=equal)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_div.grid(row=1,column=3)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_mul.grid(row=2,column=3)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_sub.grid(row=3,column=3)
button_0.grid(row=4,column=1)
button_clear.grid(row=4,column=0)
button_equal.grid(row=4,column=2)
button_add.grid(row=4,column=3)


