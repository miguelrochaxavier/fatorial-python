from customtkinter import *

def fatorial_number():
    global x
    x = entry.get()  
    try:
        x = int(x)  
        print(f'Valor salvo: {x}')
    except ValueError:
        print('Error! Insira um número válido')

def fatorial_select(value):
    print(f'Selecionado {value}')

app = CTk()
app.geometry('600x500')
app.resizable(0,0)
app.title('Calculadora Fatorial com Python e Tkinter')

CTkLabel(master=app, text="Calculadora Fatorial com Python e Tkinter", font=("Arial Bold", 20), justify="left").pack(anchor="w", pady=(43, 18), padx=(56,0))
stats_frame = CTkFrame(master=app, fg_color="transparent")
stats_frame.pack( padx=(54, 0), pady=(18, 0), anchor="nw")

btn = CTkComboBox(master=app, values=['1-Fatorial Simples', '2-Fatorial Dupla', '3-Fatorial Tripla'],)
btn.place(relx=0.2, rely=0.3, anchor='center')

entry = CTkEntry(master=app, placeholder_text='Escreva aqui...', width=300)
entry.place(relx=0.33, rely=0.4, anchor='center')

btn = CTkButton(master=app, text='Clique aqui')
btn.place(relx=0.2, rely=0.5, anchor='center')

app.mainloop()
