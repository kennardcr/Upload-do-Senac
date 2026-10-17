import tkinter as tk

janela = tk.Tk()
janela.title("Meu primeiro aplicativo")
janela.geometry("400x300")

titulo = tk.Label(
    janela,
    text=("Cadastro de alunos"),
    font=("Arial", 16, "bold")
)

def cadastrar():
    nome = campo_nome.get()
    print("Nome cadastrado:", nome)
    
botao = tk.Button(
    janela,
    text="Cadastrar",
    command=cadastrar
)

titulo.pack()
campo_nome = tk.Entry(janela)
campo_nome.pack()
nome = campo_nome.get()
print(nome)
campo_nome.delete(0, tk.END)
botao.pack()
janela.mainloop()