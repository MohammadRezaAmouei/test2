import random as r
import turtle
import tkinter as tk

c=["#961276","#036ed9","#0C5D05","#f9ed32","#5d6874","#7f00ff","#ef4136"]


frm=tk.Tk()
frm.geometry("400x500")
frm.title("draw matrix")





tcnvs=tk.Canvas(frm,width=400,height=500,bg="#e3e3e3")
tcnvs.place(x=10,y=10)
t=turtle.RawTurtle(tcnvs)
s=t.getscreen()
s.bgcolor("black")

def chengcolor():
    pass
        
        





f=110
for x in c:
    
    btn1=tk.Button(frm,text=" ",font=("Arial",12,("bold")),bg=x,command=chengcolor)
    btn1.place(x=f,y=480)
    f+=30
    
##btn2.place(x=60,y=40)
##
##btn3=tk.Button(frm,text="2",font=("Arial",12,("bold")),bg="#0C5D05")
##btn3.place(x=90,y=40)
##
##btn4=tk.Button(frm,text="3",font=("Arial",12,("bold")),bg="#f9ed32")
##btn4.place(x=120,y=40)
##
##btn5=tk.Button(frm,text="4",font=("Arial",12,("bold")),bg="#5d6874")
##btn5.place(x=150,y=40)
##
##btn6=tk.Button(frm,text="5",font=("Arial",12,("bold")),bg="#7f00ff")
##btn6.place(x=180,y=40)
##
##btn7=tk.Button(frm,text="6",font=("Arial",12,("bold")),bg="#ef4136")
##btn7.place(x=210,y=40)
##

m=[]









# creat a random matrix loxlo for colors
for j in range(10):
    l=[]
    for i in range(10):
        l.append(r.randint(0,6))
    m.append(l)
print(m)
# draw a filled rectangle      
def rect():
    t.begin_fill()
    for a in range(4):
        t.fd(20)
        t.rt(90)
    t.end_fill()
        
t.speed(0)
t.up()
t.goto(-100,150)






      

def draw_matrix():
    for f in range(10):
        for k in range(10):
            t.pencolor(c[m[f][k]])
            t.fillcolor(c[m[f][k]])
            rect()
            t.up()
            t.fd(20)
            t.down()
        t.up()
        t.backward(200)
        t.rt(90)
        t.fd(20)
        t.lt(90)

chengcolor()
draw_matrix()
