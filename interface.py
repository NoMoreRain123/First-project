import tkinter

window = tkinter.Tk()
window.geometry("1000x800")
window.title("Test")
label = tkinter.Label(window, text="Test", font=("Arial", 30))
label.pack()
window.mainloop()
