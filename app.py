from customtkinter import *
import math

def fatorial_select(choice):
    global tipo_fatorial
    tipo_fatorial = int(choice.split('-')[0])

def fatorial_number():
    try:
        n = int(entry.get())  
        if tipo_fatorial == 1:
            result = fatorial(n)
            resultado_label.configure(text=f'O fatorial de {n}! é {result}')
        elif tipo_fatorial == 2:
            result = fatorialDuplo(n)
            resultado_label.configure(text=f'O fatorial duplo de {n}!! é {result}')
        elif tipo_fatorial == 3:
            result = fatorialTripla(n)
            resultado_label.configure(text=f'O fatorial triplo de {n}!!! é {result}')
        else:
            resultado_label.configure(text='Erro: Tipo de fatorial não encontrado.')
    except ValueError:
        resultado_label.configure(text='Erro: Entrada inválida. Digite um número inteiro.')

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

def fatorialDuplo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorialDuplo(n-2)

def fatorialTripla(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorialTripla(n-3)

app = CTk()
app.geometry('600x500')
app.resizable(0,0)
app.title('Calculadora Fatorial com Python e Tkinter')

CTkLabel(master=app, text="Calculadora Fatorial com Python e Tkinter", font=("Arial Bold", 20), justify="left").pack(anchor="w", pady=(43, 18), padx=(56,0))
stats_frame = CTkFrame(master=app, fg_color="transparent")
stats_frame.pack( padx=(54, 0), pady=(18, 0), anchor="nw")

btn = CTkComboBox(master=app, values=['1-Fatorial Simples', '2-Fatorial Dupla', '3-Fatorial Tripla'], command=fatorial_select)
btn.place(relx=0.2, rely=0.3, anchor='center')

entry = CTkEntry(master=app, placeholder_text='Escreva aqui...', width=300,)
entry.place(relx=0.33, rely=0.4, anchor='center')

btn = CTkButton(master=app, text='Clique aqui', command=fatorial_number)
btn.place(relx=0.2, rely=0.5, anchor='center')

resultado_label = CTkLabel(master=app, text="", font=("Arial", 14))
resultado_label.place(relx=0.5, rely=0.6, anchor='center')

app.mainloop()
