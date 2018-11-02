# this is program create window and
# display text on it

from tkinter import *
#instance is created
root =  Tk()

#Window creation
textLabel = Label(root,text='Window Created')
textLabel.pack()

#irrtate until we close window
root.mainloop()
