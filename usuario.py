class Usuario:
    """
    Cria a nossa classe se usuário
    Iremos utilizá-la para armazenar os dados do usuário
    e senha digitados na tela de login.

    Atributos:
    user: str
        O nome do usuário digitado na tela de login.
    senha: str
        A senha do usuário digitada na tela de login.
        
    Métodos:
    getUser: str
        Retorna o nome do usuário digitado na tela de login.
    getSenha: str
        Retorna a senha do usuário digitada na tela de login.
    """
    def __init__(self, user, senha):
        self.user = user
        self.senha = senha

    def getUser(self):
        return self.user
    
    def getSenha(self):
        return self.senha