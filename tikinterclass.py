from tkinter import *
root = Tk()


class Tkinin:
    def __init__(self, rooter):
        frame = Frame(rooter)
        frame.pack()

        self.pbutton = Button(frame, text="Print", command=self.msg)
        self.pbutton.pack()

        self.cbutton = Button(frame, text="Cancel", command=self.cancel)
        self.cbutton.pack()

        self.qbutton = Button(frame, text='Quit,', command=frame.quit)
        self.qbutton.pack()

    def msg(self):
        print("Print")

    def cancel(self):
        print("Cancled")


tkin = Tkinin(root)
root.mainloop()
