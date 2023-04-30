import tkinter as tk
from tkinter import messagebox



root=tk.Tk()
root.geometry("400x400")
root.title("COUNTER")

ct=0

def countt():
    global ct
    ct +=1
    label1=tk.Label(frame1, bg="white", fg="black", text=ct, font=("Arial",28), width=11)
    label1.place(rely=0.1, relx=0.05, relheight=0.82)
    return
def resett():
    global ct  
    ct = 0
    label1=tk.Label(frame1, bg="white", fg="black", text=ct, font=("Arial",28), width=11)
    label1.place(rely=0.1, relx=0.05, relheight=0.82)

label=tk.Label(root, text="Counter", fg="white", font=("Arial",24))
label.place(rely=0.1, relx= 0.3)

frame1 = tk.Frame(root, bg="blue",width=200)
frame1.place(rely=0.3, relx=0.2, relheight=0.3)
label1=tk.Label(frame1, bg="white", fg="black", text="", font=("Arial",28), width=11)
label1.place(rely=0.1, relx=0.05, relheight=0.82)

button1 = tk.Button(root, text="count", width= 5, command=countt)
button1.place(rely=0.6, relx=0.2)

button2 = tk.Button(root, text="reset", width= 5 , command=resett)
button2.place(rely=0.6, relx=0.5)

root.mainloop()
