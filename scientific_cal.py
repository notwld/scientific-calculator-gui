import tkinter as tk
import math as m
from tkinter import messagebox 

win=tk.Tk()
win.title("Project#01")
win.resizable(height='false',width='false')
en_box=tk.Entry(win,width=50,relief='solid',bg='green',fg='black',font="lucida 10 bold")
en_box.grid(row=0,column=0,columnspan=5,padx=5,pady=10)

def click(on_print): #gets digits
    prev=en_box.get()
    en_box.delete(0,'end')
    en_box.insert(0,prev+on_print)
    return

def clear(): #clears whatever on the entery box
    en_box.delete(0,'end')
    return

def bacsp(): #clears digit one by one
    any=en_box.get()
    lenght=len(any)-1
    en_box.delete(lenght,'end')

def ev(): #evaluate the data type automatically
    answer=en_box.get()
    answer=eval(answer)
    en_box.delete(0,'end')
    en_box.insert(0,answer)
    return answer

def functions(event): #scientific calulations 
    keys=event.widget 
    text=keys["text"]
    final_ans=''
    digits=en_box.get()
    if text=='deg':
        final_ans=str(m.degrees(float(digits)))
    elif text=='sin':
        final_ans=str(m.sin(m.radians(int(digits))))
    elif text=='cos':
        final_ans=str(m.cos(m.radians(int(digits))))
    elif text=='tan':
            final_ans=str(m.tan(m.radians(int(digits))))
    elif text=='lg':
            final_ans=str(m.log10(float(digits)))
    elif text=='ln':
            final_ans=str(m.log(float(digits)))
    elif text=='x2':
            final_ans=str(float(digits)*float(digits))
    elif text=='√':
            final_ans=str(m.sqrt(float(digits)))
    elif text=='x!':
            final_ans=str(m.factorial(float(digits)))
    elif text=='1/x':
            final_ans=str(1/(float(digits)))
    elif text=='pi':
        if digits=='':
            final_ans=str(m.pi)
        else:
            final_ans=str(m.pi*float(digits))
    elif text=='e':
        if digits=='':
            final_ans=str(m.e)
        else:
            final_ans=str(m.e**float(digits))
    en_box.delete(0,'end')
    en_box.insert(0,final_ans)
            
            

#buttons

lg=tk.Button(win,text="lg",relief='raised',padx=28,pady=10,fg="white",bg="black")
lg.bind("<Button-1>",functions)
lg.grid(row=1,column=0)

ln=tk.Button(win,text="ln",relief='raised',padx=29,pady=10,fg="white",bg="black")
ln.bind("<Button-1>",functions)
ln.grid(row=1,column=1)

br1=tk.Button(win,text="(",relief='raised',padx=29,pady=10,fg="white",bg="black",command=lambda:click('('))
br1.grid(row=1,column=2)

br2=tk.Button(win,text=")",relief='raised',padx=31,pady=10,fg="white",bg="black",command=lambda:click(')'))
br2.grid(row=1,column=3)

dot=tk.Button(win,text=".",relief='raised',padx=31,pady=10,fg="white",bg="black",command=lambda:click('.'))
dot.grid(row=1,column=4)

cap=tk.Button(win,text="^",relief='raised',padx=29,pady=10,fg="white",bg="black",command=lambda:click('**'))
cap.grid(row=2,column=0)

deg=tk.Button(win,text="deg",relief='raised',padx=24,pady=10,fg="white",bg="black")
deg.bind("<Button-1>",functions)
deg.grid(row=2,column=1)

sin=tk.Button(win,text="sin",relief='raised',padx=24,pady=10,fg="white",bg="black")
sin.bind("<Button-1>",functions)
sin.grid(row=2,column=2)

cos=tk.Button(win,text="cos",relief='raised',padx=24,pady=10,fg="white",bg="black")
cos.bind("<Button-1>",functions)
cos.grid(row=2,column=3)

tan=tk.Button(win,text="tan",relief='raised',padx=24,pady=10,fg="white",bg="black")
tan.bind("<Button-1>",functions)
tan.grid(row=2,column=4)

sqrt=tk.Button(win,text="√",relief='raised',padx=29,pady=10,fg="white",bg="black")
sqrt.bind("<Button-1>",functions)
sqrt.grid(row=3,column=0)

C=tk.Button(win,text="C",relief='raised',padx=30,pady=10,fg="white",bg="black",command=lambda:clear())
C.grid(row=3,column=1)

bspc=tk.Button(win,text="⟵",relief='raised',padx=25,pady=10,fg="white",bg="black",command=lambda:bacsp())
bspc.grid(row=3,column=2)

x2=tk.Button(win,text="x2",relief='raised',padx=28,pady=10,fg="white",bg="black")
x2.bind("<Button-1>",functions)
x2.grid(row=3,column=3)

bksl=tk.Button(win,text="/",relief='raised',padx=30,pady=10,fg="white",bg="black",command=lambda:click('/'))
bksl.grid(row=3,column=4)

x1=tk.Button(win,text="x!",relief='raised',padx=28,pady=10,fg="white",bg="black")
x1.bind("<Button-1>",functions)
x1.grid(row=4,column=0)

seven=tk.Button(win,text="7",relief='raised',padx=30,pady=10,fg="green",bg="black",command=lambda:click('7'))
seven.grid(row=4,column=1)

eight=tk.Button(win,text="8",relief='raised',padx=30,pady=10,fg="green",bg="black",command=lambda:click('8'))
eight.grid(row=4,column=2)

nine=tk.Button(win,text="9",relief='raised',padx=30,pady=10,fg="green",bg="black",command=lambda:click('9'))
nine.grid(row=4,column=3)

mul=tk.Button(win,text="*",relief='raised',padx=30,pady=10,fg="white",bg="black",command=lambda:click('*'))
mul.grid(row=4,column=4)

onebx=tk.Button(win,text="1/x",relief='raised',padx=24,pady=10,fg="white",bg="black")
onebx.bind("<Button-1>",functions)
onebx.grid(row=5,column=0)

four=tk.Button(win,text="4",relief='raised',padx=30,pady=10,fg="green",bg="black",command=lambda:click('4'))
four.grid(row=5,column=1)

five=tk.Button(win,text="5",relief='raised',padx=30,pady=10,fg="green",bg="black",command=lambda:click('5'))
five.grid(row=5,column=2)

six=tk.Button(win,text="6",relief='raised',padx=30,pady=10,fg="green",bg="black",command=lambda:click('6'))
six.grid(row=5,column=3)

minus=tk.Button(win,text="-",relief='raised',padx=30,pady=10,fg="white",bg="black",command=lambda:click('-'))
minus.grid(row=5,column=4)

pi=tk.Button(win,text="pi",relief='raised',padx=28,pady=10,fg="white",bg="black")
pi.bind("<Button-1>",functions)
pi.grid(row=6,column=0)

one=tk.Button(win,text="1",relief='raised',padx=30,pady=10,fg="green",bg="black",command=lambda:click('1'))
one.grid(row=6,column=1)

two=tk.Button(win,text="2",relief='raised',padx=30,pady=10,fg="green",bg="black",command=lambda:click('2'))
two.grid(row=6,column=2)

three=tk.Button(win,text="3",relief='raised',padx=30,pady=10,fg="green",bg="black",command=lambda:click('3'))
three.grid(row=6,column=3)

plus=tk.Button(win,text="+",relief='raised',padx=29,pady=10,fg="white",bg="black",command=lambda:click('+'))
plus.grid(row=6,column=4)

exit=tk.Button(win,text="exit",relief='raised',padx=23,pady=10,fg="white",bg="purple",command=win.destroy)
exit.grid(row=7,column=0)

e=tk.Button(win,text="e",relief='raised',padx=30,pady=10,fg="white",bg="black")
e.bind("<Button-1>",functions)
e.grid(row=7,column=1)

zero=tk.Button(win,text="0",relief='raised',padx=30,pady=10,fg="green",bg="black",command=lambda: click("0"))
zero.grid(row=7,column=2)

equal=tk.Button(win,text="=",relief='raised',padx=30,pady=10,fg="white",bg="black",command=lambda:ev())
equal.grid(row=7,column=3)

def msg():
    messagebox.showinfo("Credits", "Made By Waleed And Cocomo(Well yes but actually no)..!") 

owo=tk.Button(win,text="Credits",relief='raised',padx=15,pady=10,fg="white",bg="black",command=msg)
owo.grid(row=7,column=4)


win.mainloop()
