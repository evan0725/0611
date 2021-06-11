from tkinter import *

window=Tk()
window.title("label")
window.geometry("500x400+100+15")
lab=Label(window,text="Savage love Did somebody, did somebody Break your heart? Lookin' like an angel But your savage love When you kiss me I know you don't give two fucks But I still want that"
          ,anchor=N,width=30,height=20,background="#0088ff",foreground="#ffffff",wraplength=120,justify=CENTER
          ,font=("Helvettica",10,"bold","italic",UNDERLINE))

lab.pack()
window.mainloop()