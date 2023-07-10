import tkinter as tk
from tkinter import ttk


app = tk.Tk()

app.title("Book In Shlef")
app.geometry("1200x800")
app.configure(background="#f0dc82")

#estilo
estiloBotao = ttk.Style()
estiloBotao.configure("EstiloBotao.TButton", font=('Montserrat', 18, 'bold'), fg="#391932", background="#f0dc82")

estiloLabel = ttk.Style()
estiloLabel.configure("Estilo.TLabel", font=('Montserrat', 28, 'bold'), background="#f0dc82", fg="#391932")


#pagina

frameTitulo = tk.Frame(app, padx=10, pady=10, background="#f0dc82")
frameTitulo.pack()

espaco = tk.Frame(frameTitulo, height=25, background="#f0dc82")
espaco.pack()
titulo = ttk.Label(frameTitulo ,text="Bem Vindo ao Book in Shlef!", font=('Montserrat', 28, 'bold'), background="#f0dc82", foreground="#131211")
titulo.pack()


frame = tk.Frame(app, padx=10, pady=10, background="#f0dc82")
frame.pack()
espaco = tk.Frame(frame, height=50, background="#f0dc82")
espaco.pack()
texto1 = ttk.Label(frame, text="Cadastrar-se", style="Estilo.TLabel")
texto1.pack()
email = ttk.Entry(frame, width=45)
email.pack()
espaco = tk.Frame(frame, height=50, background="#f0dc82")
espaco.pack()

texto2 = ttk.Label(frame, text="Nome de perfil", style="Estilo.TLabel")
texto2.pack()
nome = ttk.Entry(frame, width=45)
nome.pack()
espaco = tk.Frame(frame, height=50, background="#f0dc82")
espaco.pack()

texto3 = ttk.Label(frame, text="Senha", style="Estilo.TLabel")
texto3.pack()
senha = ttk.Entry(frame, width=45)
senha.pack()
espaco = tk.Frame(frame, height=50, background="#f0dc82")
espaco.pack()

texto4 = ttk.Label(frame, text="Confirmar senha", style="Estilo.TLabel")
texto4.pack()
senha2 = ttk.Entry(frame, width=45)
senha2.pack()
espaco = tk.Frame(frame, height=50, background="#f0dc82")
espaco.pack()


frame2 = tk.Frame(app, padx=10, pady=10, background="#f0dc82")
frame2.pack()

cadastrarse = ttk.Button(frame, text="Cadastrar-se", style="EstiloBotao.TButton")
cadastrarse.pack()
login = ttk.Button(frame, text="logar", style="EstiloBotao.TButton")
login.pack()


app.mainloop()