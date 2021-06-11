from tkinter import *
import tkinter

def st(num):
    if int(lab['text']) != 0:
        lab['text']-lab['text']+num
    else:
        lab['text']=num

w=Tk()
w.geometry("600x600+100+50")
w.title("ouo")
w.rowconfigure(0,weight=1)
w.rowconfigure(1,weight=1)
w.rowconfigure(2,weight=1)
w.rowconfigure(3,weight=1)
w.columnconfigure(0,weight=1)
w.columnconfigure(1,weight=1)
w.columnconfigure(2,weight=1)
w.columnconfigure(3,weight=1)

lab=Label(w,text="0",justify=RIGHT,anchor=E)
lab.grid(row=0,column=0,columnspan=3,sticky=E)


b1=Button(w,text="1",command=lambda:st('1'))
b1.grid(row=0,column=0,sticky=NSEW)
b2=Button(w,text="2",command=lambda:st('2'))
b2.grid(row=0,column=1,sticky=NSEW)
b3=Button(w,text="3",command=lambda:st('3'))
b3.grid(row=0,column=2,sticky=NSEW)
a=Button(w,text="+",command=lambda:st('+'))
a.grid(row=0,column=3,sticky=NSEW)

b4=Button(w,text="4",command=lambda:st('4'))
b4.grid(row=1,column=0,sticky=NSEW)
b5=Button(w,text="5",command=lambda:st('5'))
b5.grid(row=1,column=1,sticky=NSEW)
b6=Button(w,text="6",command=lambda:st('6'))
b6.grid(row=1,column=2,sticky=NSEW)
b=Button(w,text="-",command=lambda:st('-'))
b.grid(row=1,column=3,sticky=NSEW)

b7=Button(w,text="7",command=lambda:st('7'))
b7.grid(row=2,column=0,sticky=NSEW)
b8=Button(w,text="8",command=lambda:st('8'))
b8.grid(row=2,column=1,sticky=NSEW)
b9=Button(w,text="9",command=lambda:st('9'))
b9.grid(row=2,column=2,sticky=NSEW)
c=Button(w,text="*",command=lambda:st('*'))
c.grid(row=2,column=3,sticky=NSEW)

b10=Button(w,text="0",command=lambda:st('0'))
b10.grid(row=3,column=0,sticky=NSEW)
b11=Button(w,text=".",command=lambda:st('.'))
b11.grid(row=3,column=1,sticky=NSEW)
b12=Button(w,text="=",command=lambda:st('='))
b12.grid(row=3,column=2,sticky=NSEW)
d=Button(w,text="/",command=lambda:st('/'))
d.grid(row=3,column=3,sticky=NSEW)

w.mainloop()