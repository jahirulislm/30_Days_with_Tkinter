from tkinter import *



class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # setting a label
        text = Label(self, text="Just make it")
        text.place(x=50, y=50)

        # creating button
        exitButton = Button(self, text="Exit", command=self.clickExitButton)

        #place button at
        exitButton.place(x=0, y=0)


    def clickExitButton(self):
        exit()




root = Tk()
app =Window(root)

#set window title
root.wm_title("Tkinter window")
root.geometry("320x200")
#show window
root.mainloop()



