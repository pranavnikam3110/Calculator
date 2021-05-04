from tkinter import *

def btnclick(number):
    global operator
    operator=operator + str(number)
    text_Input.set(operator)

def clrinp():
    global operator
    operator=""
    text_Input.set("")


def btnequal():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

root=Tk()
root.title("CALCULATOR")
root.iconbitmap("ic.ico")
root.resizable(0,0)
operator=""
text_Input=StringVar()


en=Entry(root,font="arial 20 bold",textvariable=text_Input,bd=16,bg="powder blue",
              justify='right').grid(columnspan=4)


btn7=Button(root,text="7",padx=12,bd=9,fg="black",font="arial 20 bold",command=lambda:btnclick(7))
btn7.grid(row=1,column=0)

btn8=Button(root,text="8",padx=12,bd=9,fg="black",font="arial 20 bold",command=lambda:btnclick(8))
btn8.grid(row=1,column=1)

btn9=Button(root,text="9",padx=12,bd=9,fg="black",font="arial 20 bold",command=lambda:btnclick(9))
btn9.grid(row=1,column=2)

btnadd=Button(root,text="+",padx=12,bd=9,fg="black",font="arial 20 bold",command=lambda:btnclick("+"))
btnadd.grid(row=1,column=3)

# ==============================================================================

btn4=Button(root,text="4",padx=12,bd=9,fg="black",font="arial 20 bold",command=lambda:btnclick(4))
btn4.grid(row=2,column=0)

btn5=Button(root,text="5",padx=12,bd=9,fg="black",font="arial 20 bold",command=lambda:btnclick(5))
btn5.grid(row=2,column=1)

btn6=Button(root,text="6",padx=12,bd=9,fg="black",font="arial 20 bold",command=lambda:btnclick(6))
btn6.grid(row=2,column=2)

btnsub=Button(root,text="-",padx=12,bd=9,fg="black",font="arial 20 bold",command=lambda:btnclick('-'))
btnsub.grid(row=2,column=3)

# =============================================================================

btn1=Button(root,text="1",padx=12,bd=9,fg="black",font="arial 20 bold",command=lambda:btnclick(1))
btn1.grid(row=3,column=0)

btn2=Button(root,text="2",padx=12,bd=9,fg="black",font="arial 20 bold",command=lambda:btnclick(2))
btn2.grid(row=3,column=1)

btn3=Button(root,text="3",padx=12,bd=9,fg="black",font="arial 20 bold",command=lambda:btnclick(3))
btn3.grid(row=3,column=2)

btnmul=Button(root,text="*",padx=12,bd=9,fg="black",font="arial 20 bold",command=lambda:btnclick("*"))
btnmul.grid(row=3,column=3)

# =============================================================================

btnclr=Button(root,text="C",padx=12,bd=9,fg="black",font="arial 20 bold",command=clrinp)
btnclr.grid(row=4,column=0)

btn0=Button(root,text="0",padx=12,bd=9,fg="black",font="arial 20 bold",command=lambda:btnclick(0))
btn0.grid(row=4,column=1)

btneql=Button(root,text="=",padx=12,bd=9,fg="black",font="arial 20 bold",command=btnequal)
btneql.grid(row=4,column=2)

btndiv=Button(root,text="/",padx=12,bd=9,fg="black",font="arial 20 bold",command=lambda:btnclick("/"))
btndiv.grid(row=4,column=3)


root.mainloop()