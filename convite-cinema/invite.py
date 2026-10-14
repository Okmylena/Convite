
import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox


root = tk.Tk()
root.title('Acelitas1')
root.geometry('600x600')
root.configure(background='#ffc8dd')


def move_button_1(e):
  
    mouse_x = e.x_root - root.winfo_rootx()
    mouse_y = e.y_root - root.winfo_rooty()

   
    button_x = button_1.winfo_x()
    button_y = button_1.winfo_y()

  
    if (button_x - 5 <= mouse_x <= button_x + button_1.winfo_width() + 5 and
        button_y - 5 <= mouse_y <= button_y + button_1.winfo_height() + 5):

        fugir()


def fugir():
    largura = root.winfo_width() - button_1.winfo_width()
    altura = root.winfo_height() - button_1.winfo_height()

    x = random.randint(0, largura)
    y = random.randint(0, altura)

    button_1.place(x=x, y=y)


def accepted():
    messagebox.showinfo(
        "Convite aceito",
        "Uhull, te vejo amanhã gatinho, sessão das 18H30 no guarapeba!",
    )


def denied():
    fugir()


margin = Canvas(root, width=500, bg='#ffc8dd', height=100,
                bd=0, highlightthickness=0, relief='ridge')
margin.pack()

text_id = Label(
    root,
    bg='#ffc8dd',
    text='Quer ir no cinema comigo?',
    fg='#590d22',
    font=('Montserrat', 24, 'bold')
)
text_id.pack(pady=15)


button_1 = tk.Button(
    root,
    text='Não',
    bg='#ffb3c1',
    command=denied,
    relief=RIDGE,
    bd=3,
    font=('Montserrat', 14, 'bold'),
    width=8
)


button_2 = tk.Button(
    root,
    text='Sim',
    bg='#ffb3c1',
    relief=RIDGE,
    bd=3,
    command=accepted,
    font=('Montserrat', 14, 'bold'),
    width=8
)


root.update_idletasks()

button_1.place(x=195, y=220)
button_2.place(x=325, y=220)


root.bind('<Motion>', move_button_1)

root.mainloop()
