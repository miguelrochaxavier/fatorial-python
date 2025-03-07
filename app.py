import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Teste CustomTkinter")
app.geometry("400x300")

label = ctk.CTkLabel(app, text="Olá, CustomTkinter!")
label.pack(pady=20)

app.mainloop()
