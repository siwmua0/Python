from tkinter import*

root = Tk()
root.title("My GUI")
root.geometry("640x480") # 가로 x 세로 


def btncmd():
    pass


btn = Button(root ,text="클릭", command=btncmd)
btn.pack()

root.mainloop()

