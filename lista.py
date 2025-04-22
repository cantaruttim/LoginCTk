class List:

    def __init__(self, lista):
        self.itens = []

    def tamanho(self):
        """Retorna o tamanho atual da lista."""
        return len(self.itens)

    def esta_vazia(self):
        """Verifica se a lista está vazia."""
        return len(self.itens) == 0

    def adicionar(self, item):
        """Adiciona um item à lista."""
        self.itens.append(item)

    def __str__(self):
        return str(self.itens)
