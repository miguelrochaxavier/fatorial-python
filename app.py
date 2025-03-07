from customtkinter import *
from tkinter import *
from tkinter import ttk
from PIL import Image

app = CTk()
app.geometry('600x500')
app.resizable(0,0)
app.title('Calculadora Fatorial com Python e Tkinter')

CTkLabel(master=app, text="Calculadora Fatorial com Python e Tkinter", font=("Arial Bold", 20), justify="left").pack(anchor="w", pady=(43, 18), padx=(56,0))
stats_frame = CTkFrame(master=app, fg_color="transparent")
stats_frame.pack( padx=(54, 0), pady=(18, 0), anchor="nw")

btn = CTkButton(master=app, text='Clique aqui')
btn.place(relx=0.2, rely=0.8, anchor='center')

app.mainloop()
