import tkinter as tk

root = tk.Tk()


def alpha():
    print("Alpha")


def bravo():
    print("Bravo")


canvas = tk.Canvas(root, height=600, width=600, bg="light blue")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

buttonA = tk.Button(root, text="Alpha", padx=10, pady=5, fg="dark blue", bg="light pink", command=alpha)
buttonA.pack()
buttonB = tk.Button(root, text="Bravo", padx=10, pady=5, fg="dark blue", bg="light pink", command=bravo)
buttonB.pack()

root.mainloop()
