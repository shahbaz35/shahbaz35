from tkinter import *
import os

#########################

root = Tk()
root.title('PCN PAYER')
root.geometry("400x600")
canvas = Canvas(root, height=50, width=600, bg="light blue").pack()
frame = Frame(root, bg="light blue").place(relwidth=0.8, relheight=0.9, relx=0.1, rely=0.1)




def loginFunction():
    message_Label = Label
    userEmail = emailTextBox.get()
    userPassword = passwordTextBox.get()
    if userEmail == '':
        message_Label = Label(root, text="Error User Email Address is Empty").pack()
    if userPassword == '':
        message_Label = Label(root, text="Error User Password is Empty").pack()
    if userEmail != '' and userPassword != '':
        message_Label = Label(root, text="Details are being processed...").pack()


emailLabel = Label(root, text="Enter User Email: ").pack()
emailTextBox = Entry(root, width=50).pack()

passwordLabel = Label(root, text="Enter User Password: ").pack()
passwordTextBox = Entry(root, width=50).pack()

emailButton = Button(root, text=" Login ", command=loginFunction).pack()

root.mainloop()
