#
from tkinter import *
w=Tk()
w.title("Lottery")
w.resizable(0,0)
#define the function
def generate():
    from random import sample
    n=sample(range(10),6)
    label1.configure(text=n[0])
    label2.configure(text=n[1])
    label3.configure(text=n[2])
    label4.configure(text=n[3])
    label5.configure(text=n[4])
    label6.configure(text=n[5])
    btn2.configure(state="normal")
    btn1.configure(state="disabled")
def reset():
    label1.configure(text="...")
    label2.configure(text="...")
    label3.configure(text="...")
    label4.configure(text="...")
    label5.configure(text="...")
    label6.configure(text="...")
    btn1.configure(state="normal")
    btn2.configure(state="disabled")



#design the components

img=PhotoImage(file="ss.gif")
lblimage=Label(w,image=img)
label1=Label(w,text="...",width=2,font=("arial",20,"bold"),relief="sunken")
label2=Label(w,text="...",width=2,font=("arial",20,"bold"),relief="sunken")
label3=Label(w,text="...",width=2,font=("arial",20,"bold"),relief="sunken")
label4=Label(w,text="...",width=2,font=("arial",20,"bold"),relief="sunken")
label5=Label(w,text="...",width=2,font=("arial",20,"bold"),relief="sunken")
label6=Label(w,text="...",width=2,font=("arial",20,"bold"),relief="sunken")
btn1=Button(w,text="My Lucky Number",fg="red",command=generate)
btn2=Button(w,text="Reset",fg="red",command=reset,state="disabled")


#placing the components

lblimage.grid(row=1,column=1,rowspan=2)
label1.grid(row=1,column=2)
label2.grid(row=1,column=3)
label3.grid(row=1,column=4)
label4.grid(row=1,column=5)
label5.grid(row=1,column=6)
label6.grid(row=1,column=7)
btn1.grid(row=2,column=2,columnspan=4)
btn2.grid(row=2,column=6,columnspan=2)
w.mainloop()
