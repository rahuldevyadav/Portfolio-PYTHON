#In this program we will create frame
#size of widget
#and putting button on it
from tkinter import *

root= Tk()

frame = Frame(root, width=300,height =200)
# ONCE WE DEFINE BUTTON WIDTH AND HEIGHT IS DEFAULT
button = Button(frame,text='Button1')
button.pack()

frame.pack()
#
# frame2 = Frame(root,width=300,height =200)
# button2 = Button(frame2,text="default")
# button2.pack(side=LEFT)


# frame2.pack(side=BOTTOM)
root.mainloop()
