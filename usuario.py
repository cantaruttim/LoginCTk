class Usuario:
    """
    Cria a nossa classe se usuário
    """
    def __init__(self, user, senha):
        self.user = user
        self.senha = senha

    def getUser(self):
        return self.user
    
    def getSenha(self):
        return self.senha