from re import 
from turtle import clear
import parser
from tkinter import *

root = Tk()

root.title("Calculator")
display= Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)

i=0
def get_variable(num):
    global i 
    display.insert(i,num)
    i+=1
    
def clear_all():
    display.delete(0,END)   
    
def undo():
    str1 = display.get()
    if len(str1):
        nstr = str1[:-1]
        clear_all()
        display.insert(0,nstr)    
    else:
        clear_all()
        display.insert(0,"Error")    
def get_operation(opr):
    global i 
    length= len(opr)
    display.insert(i,opr)
    i+=length             
def calculate():
    entire = display.get()
    try:
        a = parser.expr(entire).compile()
        result =eval(a)
        clear_all()
        display.insert(0,result)
    except:
     clear_all()  
     display.insert(0,"Error")  


Button(root,text="7",command=lambda :get_variable(7)).grid(row=2,column=0)
Button(root,text="8",command=lambda :get_variable(8)).grid(row=2,column=1)
Button(root,text="9",command=lambda :get_variable(9)).grid(row=2,column=2)
Button(root,text="4",command=lambda :get_variable(4)).grid(row=3,column=0)
Button(root,text="5",command=lambda :get_variable(5)).grid(row=3,column=1)
Button(root,text="6",command=lambda :get_variable(6)).grid(row=3,column=2)
Button(root,text="1",command=lambda :get_variable(1)).grid(row=4,column=0)
Button(root,text="2",command=lambda :get_variable(2)).grid(row=4,column=1)
Button(root,text="3",command=lambda :get_variable(3)).grid(row=4,column=2)
Button(root,text="0",command=lambda :get_variable(0)).grid(row=5,column=0)
Button(root,text=".",command=lambda :get_variable(".")).grid(row=5,column=1)
Button(root,text="=" ,command=lambda :calculate()).grid(row=6,column=1)
Button(root,text="+",command=lambda :get_operation('+')).grid(row=5,column=2) 
Button(root,text="=>",command=lambda:undo()).grid(row=2,column=3)
Button(root,text="-",command=lambda :get_operation('-')).grid(row=3,column=3)
Button(root,text="*",command=lambda :get_operation('*')).grid(row=4,column=3)
Button(root,text="/",command=lambda :get_operation('/')).grid(row=5,column=3)
Button(root,text="AC",command=lambda:clear_all()).grid(row=6,column=0)


root.mainloop()