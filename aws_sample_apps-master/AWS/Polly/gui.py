import tkinter as tk

window = tk.Tk()

label = tk.Label(
    text='Hi, this is Justin \n Remmenber you\'re AWSome! \n Now yype something...',
    fg='orange',
    bg='black',
    width=55,
    height=5
)

button = tk.Button(
    text='Submit',
    width=25,
    height=2,
    bg='orange',
    fg='black'
)

entry = tk.Entry(
    fg='orange',
    bg='white',
    width=30
)

label.pack()
entry.pack()
button.pack()

msg = entry.get()
# entry.delete(0,5)
print(msg)
window.mainloop()
