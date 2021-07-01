import tkinter as tk

window = tk.Tk()

# greeting = tk.Label(text='Hi, this is Justin')
# greeting.pack()

label = tk.Label(
    text='Hi, thisis Justin you\'re doing AWSome',
    foreground='orange',
    background='black',
    width=50,
    height=50
)

label.pack()

window.mainloop()
