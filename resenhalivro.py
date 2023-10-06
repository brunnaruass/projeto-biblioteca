import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk

class Pessoa:
    def __init__(self, nome, idade, genero_favorito=None):
        self.nome = nome
        self.idade = idade
        self.genero_favorito = genero_favorito

class Autor(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

class Genero:
    def __init__(self, nome, descricao, subgeneros=[]):
        self.nome = nome
        self.descricao = descricao
        self.subgeneros = subgeneros
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

class Livro:
    def __init__(self, titulo, autor, genero, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano_publicacao = ano_publicacao
        self.resenhas = []
        self.genero.adicionar_livro(self)

    def adicionar_resenha(self, resenha):
        self.resenhas.append(resenha)

class Resenha:
    def __init__(self, livro, autor, conteudo, rating):
        self.livro = livro
        self.autor = autor
        self.conteudo = conteudo
        self.rating = rating

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Biblioteca")
        self.geometry("600x400")

        self.generos = []
        self.livros = []
        self.pessoas = []
        self.resenhas = []

        self.titulo_var = tk.StringVar()
        self.autor_var = tk.StringVar()
        self.genero_var = tk.StringVar()
        self.ano_var = tk.StringVar()
        self.resenha_var = tk.StringVar()
        self.rating_var = tk.StringVar()
        self.pessoa_nome_var = tk.StringVar()
        self.pessoa_idade_var = tk.StringVar()
        self.pessoa_genero_favorito_var = tk.StringVar()

       
        

        self.criar_interface()


    def criar_interface(self):
        # Frame para adicionar livro
        frame_livro = ttk.LabelFrame(self, text="Adicionar Livro")
        frame_livro.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(frame_livro, text="Título do livro:").grid(row=0, column=0)
        ttk.Entry(frame_livro, textvariable=self.titulo_var).grid(row=0, column=1)

        ttk.Label(frame_livro, text="Autor:").grid(row=1, column=0)
        ttk.Entry(frame_livro, textvariable=self.autor_var).grid(row=1, column=1)

        ttk.Label(frame_livro, text="Gênero:").grid(row=2, column=0)
        ttk.Entry(frame_livro, textvariable=self.genero_var).grid(row=2, column=1)

        ttk.Label(frame_livro, text="Ano de publicação:").grid(row=3, column=0)
        ttk.Entry(frame_livro, textvariable=self.ano_var).grid(row=3, column=1)

        ttk.Button(frame_livro, text="Adicionar Livro", command=self.adicionar_livro).grid(row=4, column=0, columnspan=2)

        # Frame para adicionar resenha
        frame_resenha = ttk.LabelFrame(self, text="Adicionar Resenha")
        frame_resenha.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ttk.Label(frame_resenha, text="Autor da resenha:").grid(row=0, column=0)
        ttk.Entry(frame_resenha, textvariable=self.resenha_var).grid(row=0, column=1)

        ttk.Label(frame_resenha, text="Avaliação (0-5):").grid(row=1, column=0)
        ttk.Entry(frame_resenha, textvariable=self.rating_var).grid(row=1, column=1)

        ttk.Label(frame_resenha, text="Resenha (até 30 linhas):").grid(row=2, column=0)
        self.texto_resenha = scrolledtext.ScrolledText(frame_resenha, wrap=tk.WORD, width=30, height=10)
        self.texto_resenha.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(frame_resenha, text="Livro da resenha:").grid(row=3, column=0)
        self.combo_livro = ttk.Combobox(frame_resenha, values=[livro.titulo for livro in self.livros])
        self.combo_livro.grid(row=3, column=1)

        ttk.Button(frame_resenha, text="Adicionar Resenha", command=self.adicionar_resenha).grid(row=4, column=0, columnspan=2)

        # Frame para visualizar livros e resenhas
        frame_visualizar = ttk.LabelFrame(self, text="Visualizar Livros e Resenhas")
        frame_visualizar.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        ttk.Button(frame_visualizar, text="Visualizar Livros e Resenhas", command=self.visualizar_livros_resenhas).pack(padx=10, pady=10)

        

        # Configuração de expansão de linhas e colunas
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def adicionar_livro(self):
        titulo = self.titulo_var.get()
        autor = self.autor_var.get()
        genero = self.genero_var.get()
        ano_publicacao = self.ano_var.get()

        autor_objeto = Autor(autor, 30)  # Assumindo que a idade do autor é 30
        genero_objeto = Genero(genero, "Ficção")  # Assumindo que a descrição do gênero é "Ficção"
        novo_livro = Livro(titulo, autor_objeto, genero_objeto, ano_publicacao)
        self.livros.append(novo_livro)

        messagebox.showinfo("Sucesso", "Livro adicionado com sucesso!")

    def adicionar_resenha(self):
        autor_resenha = self.resenha_var.get()
        rating = self.rating_var.get()
        texto_resenha = self.texto_resenha.get("1.0", tk.END)[:30]  # Limita o texto a 30 linhas
        livro_resenha = None

        for livro in self.livros:
            if livro.titulo == self.combo_livro.get():
                livro_resenha = livro
                break

        if livro_resenha:
            autor_objeto = Autor(autor_resenha, 30)  # Assumindo que a idade do autor é 30
            nova_resenha = Resenha(livro_resenha, autor_objeto, texto_resenha, rating)
            livro_resenha.adicionar_resenha(nova_resenha)
            self.resenhas.append(nova_resenha)

            messagebox.showinfo("Sucesso", "Resenha adicionada com sucesso!")
        else:
            messagebox.showerror("Erro", "Livro não encontrado.")

    def visualizar_livros_resenhas(self):
        if not self.livros:
            messagebox.showinfo("Livros e Resenhas", "Nenhum livro encontrado.")
            return

        livro_resenha_info = []

        for livro in self.livros:
            autor = livro.autor.nome
            titulo = livro.titulo
            genero = livro.genero.nome
            resenhas = []

            for resenha in livro.resenhas:
                autor_resenha = resenha.autor.nome
                rating_resenha = resenha.rating
                conteudo_resenha = resenha.conteudo
                resenhas.append(f"Autor da Resenha: {autor_resenha}\nAvaliação: {rating_resenha}\nResenha: {conteudo_resenha}")

            livro_info = f"Título: {titulo}\nAutor: {autor}\nGênero: {genero}\nResenhas:\n"
            livro_info += "\n".join(resenhas) + "\n\n"
            livro_resenha_info.append(livro_info)

        livro_resenha_text = "\n".join(livro_resenha_info)
        
        # Crie uma janela separada para exibir as informações de livros e resenhas
        janela_info = tk.Toplevel(self)
        janela_info.title("Livros e Resenhas")
        janela_info.geometry("800x600")

        info_text = scrolledtext.ScrolledText(janela_info, wrap=tk.WORD, width=80, height=25)
        info_text.pack(padx=10, pady=10)
        info_text.insert(tk.END, livro_resenha_text)
        info_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
