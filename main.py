import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage

# Criando janela
janela = tk.Tk()
janela.title("Meu app de Tarefas")
janela.configure(bg="#f0f0f0")
janela.geometry("500x600")

font_cabecalho = font.Font(family="Garamond", size=24, weight="bold", )
rotulo_cabecalho = tk.Label(janela, text="Meu App de Tarefas",
                            font=font_cabecalho, bg="#f0f0f0", fg="#333").pack(pady=20)


frame = tk.Frame(janela, bg="#f0f0f0").pack(pady=11)

entrada_tarefa = tk.Entry(frame, font=("Garamond", 14),
                          relief=tk.FLAT, bg="white", fg="grey", width=30)
entrada_tarefa.pack(side=tk.LEFT, padx=10)

botao_adicionar = tk.Button(frame, text="Adicionar Tarefas", bg="#4caf50",
                            fg="white", height=1, width=15, font=("Roboto", 11), relief=tk.FLAT)
botao_adicionar.pack(side=tk.LEFT, padx=10)


# Criar um frame para a lista de tarefas com rolagem
frame_lista_tarefas = tk.Frame(janela, bg="white")
frame_lista_tarefas. pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas = tk.Canvas(frame_lista_tarefas, bg="white")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)



janela.mainloop()
