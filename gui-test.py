# _*_ Coding:utf-8 _*_

#<span style="font-size:24px;" deep="6" >


from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
    def _init_(self,master = None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel = Label(self,text = 'hi')
        self.helloLabel.pack()
        self.quitButton = Button(self,text = 'Quit',command = self.quit)
        self.quitButton.pack()
        self.input = Entry(self)
        self.input.pack()
        self.nameButton = Button(self,text = 'hello',command = self.hello)
        self.nameButton.pack()
    def hello(self):
        name = self.input.get()
        messagebox.showinfo('Message','hello,%s' &name)
app = Application()
app.master.title("hello")

app.mainloop()


