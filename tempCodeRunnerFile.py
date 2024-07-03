import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage

# Criando janela
janela = tk.Tk()
janela.title("Meu app de Tarefas")
janela.configure(bg="#f0f0f0")
janela.geometry("500x600")

# Criando fonte para o cabeçalho
font_cabecalho = font.Font(family="Garamond", size=24, weight="bold")

# Adicionando rótulo do cabeçalho
rotulo_cabecalho = tk.Label(janela, text="Meu App de Tarefas", font=font_cabecalho, bg="#f0f0f0", fg="#333")
rotulo_cabecalho.pack(pady=20)

janela.mainloop()