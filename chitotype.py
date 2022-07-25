from cProfile import label
import tkinter as tk
import nepali_transliteration as nt
def onReturn(event):
    print("input taken")
    val = entry1.get()
    print("The text input is: ",val)
    newval = nt.convert(val)
    print("The converted text is",newval)
    entry2.insert(0,newval)

window = tk.Tk()
window.geometry('600x400')
window.title("Chitotype")
tt1 = "Enter text here"
l= tk.Label(window, text=tt1)
l.pack()
entry1 = tk.Entry(window, width = 300)
entry1.bind("<Return>",onReturn)
entry1.pack()
tt = "Converted"
l1= tk.Label(window, text=tt)
l1.pack()
entry2 = tk.Entry(window, width = 300)
entry2.pack()

window.mainloop()