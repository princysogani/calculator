from tkinter import*
import tkinter as tkr
app =tkr.Tk()
app.title("CALCI")
app.geometry('410x600')
tkr.Label(app,text="CALCULATOR",font=("Arial",20),width=12,height=1,bg='black',fg='white').pack()

def run():
    print('entry box',en1.get())

def click(operator):
    global x
    x= x+str(operator)
    data.set(x)

def clear():
    global x
    x=""
    data.set(x)

def equal():
    global x
    evaluate= eval(x)
    data.set(evaluate)

x=""
data=StringVar()
en1=Entry(app,textvariable=data,font=(30),width=18)
en1.pack()


tkr.Button(app,text="/",command=lambda:click("/"),width=5,height=2,font=("arial",18),bg="white",fg="black").place(x=320,y=100)
tkr.Button(app,text="+",command=lambda:click("+"),width=5,height=2,font=("arial",18),bg="white",fg="black").place(x=320,y=400)
tkr.Button(app,text="-",command=lambda:click("-"),width=5,height=2,font=("arial",18),bg="white",fg="black").place(x=320,y=300)
tkr.Button(app,text="*",command=lambda:click("*"),width=5,height=2,font=("arial",18),bg="white",fg="black").place(x=320,y=200)

tkr.Button(app,text="0",command=lambda:click("0"),width=5,height=2,font=("arial",16),bg="grey",fg="black").place(x=120,y=500)
tkr.Button(app,text="1",command=lambda:click("1"),width=5,height=2,font=("arial",16),bg="grey",fg="black").place(x=18,y=400)
tkr.Button(app,text="2",command=lambda:click("2"),width=5,height=2,font=("arial",16),bg="grey",fg="black").place(x=120,y=400)
tkr.Button(app,text="3",command=lambda:click("3"),width=5,height=2,font=("arial",16),bg="grey",fg="black").place(x=220,y=400)

tkr.Button(app,text="4",command=lambda:click("4"),width=5,height=2,font=("arial",16),bg="grey",fg="black").place(x=18,y=300)
tkr.Button(app,text="5",command=lambda:click("5"),width=5,height=2,font=("arial",16),bg="grey",fg="black").place(x=120,y=300)
tkr.Button(app,text="6",command=lambda:click("6"),width=5,height=2,font=("arial",16),bg="grey",fg="black").place(x=220,y=300)
tkr.Button(app,text="7",command=lambda:click("7"),width=5,height=2,font=("arial",16),bg="grey",fg="black").place(x=18,y=200)
tkr.Button(app,text="8",command=lambda:click("8"),width=5,height=2,font=("arial",16),bg="grey",fg="black").place(x=120,y=200)
tkr.Button(app,text="9",command=lambda:click("9"),width=5,height=2,font=("arial",16),bg="grey",fg="black").place(x=220,y=200)
tkr.Button(app,text="%",command=lambda:click("%"),width=5,height=2,font=("arial",16),bg="white",fg="black").place(x=220,y=100)
tkr.Button(app,text="AC",command=lambda:clear(),width=5,height=2,font=("arial",16),bg="white",fg="black").place(x=120,y=100)
tkr.Button(app,text=".",command=lambda:click("."),width=5,height=2,font=("arial",16),bg="white",fg="black").place(x=220,y=500)

tkr.Button(app,text="=",command=lambda:equal(),width=5,height=2,font=("arial",18),bg="white",fg="black").place(x= 320,y=500)

app.mainloop()




