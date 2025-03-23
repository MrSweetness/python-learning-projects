import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x200")

label = tk.Label(root, text="Hello, Tkinter")
label.grid(row=1, column=0, columnspan=4)

tk.Entry(root).grid(row=2, column=0, columnspan=4)

tk.Button(root, text="+").grid(row=3, column=0)
tk.Button(root, text="-").grid(row=3, column=1)
tk.Button(root, text="*").grid(row=3, column=2)
tk.Button(root, text="/").grid(row=3, column=3)
tk.Button(root, text="Clear").grid(row=4, column=0, columnspan=4)

tk.Button(root, text="Close", command=root.quit).grid(row=5, column=0, columnspan=4)

root.mainloop()