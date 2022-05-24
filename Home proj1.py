from tkinter import *
root = Tk()
root.title("idk")
root.geometry("500x500")

HLabel = Label(root, text = "Drivers Licence", background = "black", foreground = "white", width = "500", height = "3")
HLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)

IDL = Label(root, text = "ID = 6568756202")
IDL.place(relx = 0.11, rely = 0.2, width = "500", height = "25", anchor = CENTER)

NL = Label(root, text = "Name = Aarav Bhagwat")
NL.place(relx = 0.13, rely = 0.4, anchor = CENTER)

DOBL = Label(root, text = "Date of birth = 22 Febuary 2010")
DOBL.place(relx = 0.17, rely = 0.5, anchor = CENTER)

PINL = Label(root, text = "Pin = 4349")
PINL.place(relx = 0.06, rely = 0.6, anchor = CENTER)

ADL = Label(root, text = "Address = London")
ADL.place(relx = 0.1, rely = 0.7, anchor = CENTER)

ACL = Label(root, text = "Authorisation to drive  = Porche 911 turbo S")
ACL.place(relx = 0.01, rely = 0.8)

root.mainloop()