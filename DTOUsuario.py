class DTOUsuario:
    """
    
    Classe responsável por extrair os dados do banco

    """
    def __init__(self, id, usuario, senha):
        self.id = id
        self.usuario = usuario
        self.senha = senha

    def getDTOId(self):
        return self.id
    
    def setDTOId(self, id):
        self.id = id
    
    def getDTOUsuario(self):
        return self.usuario
    
    def setDTOUsuario(self, usuario):
        self.usuario = usuario
    
    def getDTOSenha(self):
        return self.senha
    
    def setDTOSenha(self, senha):
        self.senha = senha

    def __str__(self):
        return f"""
            DTOUsuario(
                nome={self.usuario}, 
                senha={self.senha}
            )"""