from app import usuarioEntry, senhaEntry, cursor
from DTOUsuario import DTOUsuario

usuario = usuarioEntry.get()
senha = senhaEntry.get() 


dtoUsuario = DTOUsuario(usuario, senha)
