from tkinter import *
from system import center_window

def menu():
    title = Tk()
    title.title("Maze")
    title.resizable(False, False)
    title.geometry("320x300")

    center_window(title)

    form = Frame(title, width=640, height=640, bg='#222831', bd=2, relief='ridge')
    form.pack(padx=40, pady=40)
    form.pack_propagate(False)

    label = Label(form, text="Enter grid size:", font=("Segoe UI", 16), fg="#eeeeee", bg="#222831")
    label.grid(row=0, column=0, pady=(20, 10), sticky="w", padx = 35)

    grid_input = Entry(form, font=("Segoe UI", 14), width=10, bg="#393e46", fg="#eeeeee", insertbackground="#eeeeee", relief="solid", bd=1)
    grid_input.grid(row=1, column=0, pady=(0, 20), sticky="w", padx=55)
    result = []

    def on_submit():
        for widget in form.grid_slaves(row=2, column=0):
            widget.destroy()
        try:
            value = int(grid_input.get())
            result.append(value)
            title.destroy()
        except ValueError:
            alert = Label(form, text="Please, insert digits only", font=("Segoe UI", 12), fg="#ff2e63", bg="#222831")
            alert.grid(row=2, column=0, pady=(0, 10), sticky="w", padx = 15)

    submit = Button(form, text="Start", command=on_submit, font=("Segoe UI", 14), bg="#00adb5", fg="#eeeeee", activebackground="#393e46", activeforeground="#eeeeee", relief="raised", bd=2, cursor="hand2")
    submit.grid(row=3, column=0, pady=(10, 0), sticky="w", padx=80)

    title.mainloop()

    if result:
        print(result[0])
        return result[0]
    else:
        print("No valid input.")
        return None
