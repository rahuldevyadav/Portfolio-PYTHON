#create login page
from tkinter import *

root = Tk()

name = Label(root, text = "User Name :")
entry1=Entry(root)
name.grid(row=1,column=0,sticky=E)
entry1.grid(row=1,column=1)

pw =Label(root,text = "Password:")
entry2=Entry(root)
pw.grid(row=2,column=0,sticky=E)
entry2.grid(row=2,column=1)

c=Checkbutton(root,text="Keep Me Logged In")
c.grid(columnspan=2)

button = Button(root, text ='Log In' )
button.grid(columnspan=2)

root.mainloop()
