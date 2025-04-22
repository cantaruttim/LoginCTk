# aparência
# janela principal
# cmapos
# funcinalidades
# inicar a aplicação

import customtkinter as ctk
import mysql.connector
from DTOUsuario import DTOUsuario
from dotenv import load_dotenv
import os
load_dotenv()

hostMysql = os.getenv('HOST_MYSQL')
userMysql = os.getenv('USER_MYSQL')
password = os.getenv('SENHA_MYSQL')
dbMysql = os.getenv('DB_MYSQL')

ctk.set_appearance_mode('dark')

def conexao(host, user, password, database):
    conexao = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return conexao

conexao = conexao(hostMysql, userMysql, password, dbMysql)
cursor = conexao.cursor()


# CREATE
def cadastrar_usuario():
    
    print(f"""
        Cadastrando Usuário ...
          """)
    
    # Usuário e Senha extraídos do banco de dados
    usuario = usuarioEntry.get()
    senha = senhaEntry.get()

    campoFeedCadastro.configure(
        text="Usuário cadastrado com sucesso!",
        text_color="green"
    )

    # INSERT
    sqlInsert = "INSERT INTO login (usuario, senha) VALUES (%s, %s)"
    cursor.execute(sqlInsert, (usuario, senha))

    conexao.commit()

    usuarioEntry.delete(0, 'end')
    senhaEntry.delete(0, 'end')


# READ
def validar_login():

    print(f"""
        Validando informações para Login ... 
          Usuário digitado  
          Senha digitada  
        """)

    # Usuário e Senha extraídos do banco de dados
    usuario = usuarioEntry.get()
    senha = senhaEntry.get()

    sqlSelect = f'''    
                    SELECT 
                        id, usuario, senha 
                    FROM login 
                    WHERE usuario LIKE "{usuario}%" 
                        AND senha LIKE "{senha}%"     
                '''

    cursor.execute(sqlSelect)
    resultado = cursor.fetchall()

    # Variáveis DTO
    if not resultado:
        print("Novo Usuário")
    else:
        idDTO = int(resultado[0][0])
        usuarioDTO = resultado[0][1]
        senhaDTO = resultado[0][2]

        userDTO = DTOUsuario(
            id=idDTO,
            usuario=usuarioDTO,
            senha=senhaDTO
        )

    if (usuarioEntry.get() == userDTO.getDTOUsuario()) and (senhaEntry.get() == userDTO.getDTOSenha()):
        campoFeedBackLogin.configure(
            text="Login realizado com sucesso!",
            text_color="green"
        )
        conexao.commit()
    else:
        campoFeedBackLogin.configure(
            text="Usuário ou Senha incorretos!",
            text_color="red"
        )

        usuarioEntry.delete(0, 'end')
        senhaEntry.delete(0, 'end')
        print(f"Usuário ou Senha incorreto!")


    # READ
    sqlSelect = f'''
        SELECT 
            id, usuario, senha 
        FROM login 
        WHERE usuario LIKE "{usuario}%"
            AND senha LIKE "{senha}%"
    '''

    cursor.execute(sqlSelect)
    resultado = cursor.fetchall()

    print(f""" Dados encontrados no Banco:
        Id :  {resultado[0][0]}
        Usuário :  {resultado[0][1]}
        Senha :  {resultado[0][2]}
    """)

    usuarioEntry.delete(0, 'end')
    senhaEntry.delete(0, 'end')
    
#### TELA ####
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
                          placeholder_text="Digite sua senha",
                          show="*")
senhaEntry.pack(pady=10)
buttonLogin = ctk.CTkButton(app, 
                            text="Login", 
                            command=validar_login)
buttonLogin.pack(pady=10)

buttonCadastro = ctk.CTkButton(app, 
                            text="Cadastrar",
                            hover=True,
                            command=cadastrar_usuario)
buttonCadastro.pack(pady=10)

campoFeedBackLogin = ctk.CTkLabel(app, 
                                  text='')
campoFeedBackLogin.pack(pady=10)

campoFeedCadastro = ctk.CTkLabel(app, 
                                  text='')
campoFeedCadastro.pack(pady=10)

app.mainloop()
