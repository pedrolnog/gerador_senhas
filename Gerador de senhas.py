#TODO organizar lista de senhas

import string
import secrets
import threading
import tkinter as tk
from tkinter import Tk
from tkinter import ttk

pswd = []

def pswgen(chars=string.ascii_letters + string.digits + '@!#_%.'):
    size = qntcar.get()
    sizet = int(size)
    psw = "\n"
    psw = psw + ''.join(secrets.choice(chars) for _ in range(sizet))
    pswd.append(psw)
    lbl_result["text"] += psw

def copiar():
    txt = lbl_result["text"]
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(txt[8:])
    r.update()
    r.destroy()

def deletar():
    lbl_result['text'] = 'Senhas:'

def Thrpswgen():
    threading.Thread(target=pswgen).start()

window = tk.Tk()
window.title("Gerador de senhas")
window.resizable(width=False, height=False)

frame = ttk.Frame(master=window)
qntcar = ttk.Entry(master=frame, width=23)

txt = tk.Label(master=frame, text="Quantidade de caracteres:")
lbl_result = tk.Label(master=window, text='Senhas:')


btn = ttk.Button(
    master=window,
    text='\N{RIGHTWARDS BLACK ARROW}',
    command=Thrpswgen,

    width=7
)

copia = ttk.Button(
    master=window,
    text='📋',
    command=copiar,

    width=7
)

deletar = ttk.Button(
    master=window,
    text='✖',
    command=deletar,

    width=7
)

frame.grid(row=0, column=0)

txt.grid(row=0, column=1, padx=5, pady=0, sticky='nw')
qntcar.grid(row=0, column=1, padx=5, pady=(23, 0), sticky='nw')

btn.grid(row=0, column=2, pady=(0, 0),  sticky='nw')
copia.grid(row=0, column=2, pady=(27, 0), sticky='nw')
deletar.grid(row=0, column=2, pady=(54, 0), sticky='nw')

lbl_result.grid(row=0, column=3, padx=15, pady=(0, 35), sticky='n')


window.mainloop()
