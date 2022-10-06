from tkinter import Menu, Tk



root = Tk()
mymenu = Menu(root)
root.config(menu=mymenu)
submenu = Menu(mymenu)

#functions
def printnw():
    print("New Text File")
def printn():
    print("New File")
def printw():
    print("New Window")
def printo():
    print("Open File")  
def printof():
    print("Open Folder")     
def printor():
    print("Open Recent")  
    
                     

mymenu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New Text File",command=printnw)
submenu.add_command(label="New File",command=printn)
submenu.add_separator()
submenu.add_command(label="New Window",command=printw)
submenu.add_command(label="Open File",command=printo)
submenu.add_separator()
submenu.add_command(label="Open Folder",command=printof)
submenu.add_command(label="Open Recent",command=printor)

def printed1():
    print("Undo") 
def printed2():
    print("Redo")  
def printed3():
    print("Cut") 
def printed4():
    print("Copy")  
def printed5():
    print("Undo") 
def printed6():
    print("Undo")               
    
newmenu = Menu(mymenu)
mymenu.add_cascade(label="Edit",menu = newmenu)
newmenu.add_command(label="Undo",command=printed1)
newmenu.add_command(label="Redo",command=printed2)
newmenu.add_separator()
newmenu.add_command(label="Cut",command=printed3)
newmenu.add_command(label="Copy",command=printed4)
newmenu.add_separator()
newmenu.add_command(label="Find",command=printed5)
newmenu.add_command(label="Replace",command=printed6)


def prints1():
    print("Select All") 
def prints2():
    print("Expand")  
def prints3():
    print("Shrink") 
def prints4():
    print("Copy L")  
def prints5():
    print("Move L") 
def prints6():
    print("Duplicate") 
    
    

semenu = Menu(mymenu)
mymenu.add_cascade(label="Selection",menu = semenu)
semenu.add_command(label="Select All",command=prints1)
semenu.add_command(label="Expand",command=prints2)
semenu.add_separator()
semenu.add_command(label="Shrink",command=prints3)
semenu.add_command(label="Copy L",command=prints4)
semenu.add_separator()
semenu.add_command(label="Move L",command=prints5)
semenu.add_command(label="Duplicate",command=prints6)
semenu.add_command(label="Exit",command=root.destroy)

def printv1():
    print("Command Pallete") 
def printv2():
    print("Open View")  
def printv3():
    print("Appearence") 
def printv4():
    print("Editor Layout")  
def printv5():
    print("Explorer") 
def printv6():
    print("Search") 

Vmenu = Menu(mymenu)
mymenu.add_cascade(label="View",menu = Vmenu)
Vmenu.add_command(label="Command Pallete",command=printv1)
Vmenu.add_command(label="Open View",command=printv2)
Vmenu.add_separator()
Vmenu.add_command(label="Appearence",command=printv3)
Vmenu.add_command(label="Editor Layout",command=printv4)
Vmenu.add_separator()
Vmenu.add_command(label="Explorer",command=printv5)
Vmenu.add_command(label="Search",command=printv6)    

def printg1():
    print("Back") 
def printg2():
    print("Forward")  
def printg3():
    print("Go to File") 
def printg4():
    print("Last Edit")  
def printg5():
    print("Switch Edit") 
def printg6():
    print("Switch Group") 

Gmenu = Menu(mymenu)
mymenu.add_cascade(label="Go",menu = Gmenu)
Gmenu.add_command(label="Back",command=printg1)  
Gmenu.add_command(label="Forward",command=printg2)
Gmenu.add_command(label="Last Edit",command=printg3)
Gmenu.add_separator()
Gmenu.add_command(label="Switch Edit",command=printg4)
Gmenu.add_command(label="Switch Group",command=printg5)
Gmenu.add_separator()
Gmenu.add_command(label="Go to File",command=printg6)


root.mainloop()

