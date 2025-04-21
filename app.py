# aparência
# janela principal
# cmapos
# funcinalidades
# inicar a aplicação

import customtkinter as ctk
import mysql.connector
from dados import *
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


# CRUD
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
    print("Id extraído: ", int(resultado[0][0]))
    print("Usuário extraído: ", str(resultado[0][1]))
    print("Senha extraído: ", str(resultado[0][2]))

    # Variáveis DTO
    idDTO = int(resultado[0][0])
    usuarioDTO = resultado[0][1]
    senhaDTO = resultado[0][2]

    userDTO = usuarioDTO(
        id=idDTO,
        usuario=usuarioDTO,
        senha=senhaDTO
    )

    ### se esses valores forem iguais, então dizer que o usuário e senha existem
    ### caso contrário insere

    # os valores esperados para a parte do "" são os valores retirados do banco de dados
    if usuarioEntry.get() == userDTO.getDTOUsuario() and senhaEntry.get() == userDTO.getDTOSenha():
        campoFeedBackLogin.configure(
            text="Login realizado com sucesso!",
            text_color="green"
        )

        if resultado.is_empty():
            print(f"Usuário ou Senha não existe!")

            # INSERT
            sqlInsert = "INSERT INTO login (usuario, senha) VALUES (%s, %s)"
            cursor.execute(sqlInsert, (usuarioEntry.get(), senhaEntry.get()))

            usuarioEntry.delete(0, 'end')
            senhaEntry.delete(0, 'end')

            print(f"Usuário e Senha inseridos com sucesso!")
        else:
            print(f"Login realizado com sucesso!")
            
        conexao.commit()


    else:
        campoFeedBackLogin.configure(
            text="Usuário ou Senha incorretos!",
            text_color="red"
        )

        usuarioEntry.delete(0, 'end')
        senhaEntry.delete(0, 'end')

        print(f"Usuário ou Senha incorreto!")



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

campoFeedBackLogin = ctk.CTkLabel(app, 
                                  text='')
campoFeedBackLogin.pack(pady=10)

app.mainloop()
