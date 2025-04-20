# aparência
# janela principal
# cmapos
# funcinalidades
# inicar a aplicação

import customtkinter as ctk
ctk.set_appearance_mode('dark')

def validar_login():
    user = usuarioEntry.get()
    senha = senhaEntry.get()

    if user == "Matheus" and senha == "024689":
        campoFeedBackLogin.configure(
            text="Login realizado com sucesso!",
            text_color="green"
        )
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
