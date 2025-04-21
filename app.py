# aparência
# janela principal
# cmapos
# funcinalidades
# inicar a aplicação

import customtkinter as ctk
import mysql.connector
ctk.set_appearance_mode('dark')

def conexao(host, user, password, database):
    conexao = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return conexao
conexao = conexao('localhost', 'root', '12102021', 'aulas')
cursor = conexao.cursor()

def validar_login():

    print(f"""
        Validando Login ... 
          Usuário digitado: {usuarioEntry.get()} 
          Senha digitada: {senhaEntry.get()} 
        """)

    if usuarioEntry.get() == "Matheus" and senhaEntry.get() == "024689":
        campoFeedBackLogin.configure(
            text="Login realizado com sucesso!",
            text_color="green"
        )

        ## INSERT
        sql = f'INSERT INTO login (usuario, senha) VALUES ("{usuarioEntry.get()}", "{senhaEntry.get()}")'
        cursor.execute(sql)
        conexao.commit()
        print(f"Usuário e Senha inseridos com sucesso!")


    else:
        campoFeedBackLogin.configure(
            text="Usuário ou Senha incorretos!",
            text_color="red"
        )

app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

lblUsuario = ctk.CTkLabel(app, text='Usuário:')
lblUsuario.pack(pady=10)

usuarioEntry = ctk.CTkEntry(app, 
                            placeholder_text="Digite o seu usuário")
usuarioEntry.pack(pady=10)

lblSenha = ctk.CTkLabel(app, text='Senha:')
lblSenha.pack(pady=10)
senhaEntry = ctk.CTkEntry(app, 
                          placeholder_text="Digite sua senha")
senhaEntry.pack(pady=10)


buttonLogin = ctk.CTkButton(app, 
                            text="Login", 
                            command=validar_login)
buttonLogin.pack(pady=10)

campoFeedBackLogin = ctk.CTkLabel(app, 
                                  text='')
campoFeedBackLogin.pack(pady=10)

app.mainloop()





