from node import Node

class Pilha():
    
    def __init__(self):
        """Cria a pilha vazia"""
        self.topo = None

    def esta_vazia(self):
        return not self.topo

    def push(self,dado):
        novo = Node(dado)
        novo.prox = self.topo
        self.topo = novo

    def pop(self):
        if not self.esta_vazia():
            aux = self.topo
            self.topo = self.topo.prox
            dado = aux.item
            del aux
            return dado

    def top(self):
        if not self.esta_vazia():
            return self.topo.item

    def destruir(self):
        while not self.esta_vazia():
            self.pop()

    def imprimir(self):
        aux = Pilha()
        while not self.esta_vazia():
            print(self.top())
            aux.push(self.pop())

        while not aux.esta_vazia():
            self.push(aux.pop())

    def buscar(self, info):
        aux = Pilha()
        achou = False
        while not self.esta_vazia():
            if self.top() == info:
                achou = True
                break
            aux.push(self.pop())

        while not aux.esta_vazia():
            self.push(aux.pop())
        return achou

    def editar(self, info, novo_valor):
        aux = Pilha()
        editado = False
        while not self.esta_vazia():
            if self.top() == info:
                self.pop()
                self.push(novo_valor)
                editado = True
                break
            aux.push(self.pop())

        while not aux.esta_vazia():
            self.push(aux.pop())
        return editado

    def remover(self, info):
        aux = Pilha()
        removido = False
        while not self.esta_vazia():
            if self.top() == info:
                self.pop()
                removido = True
                break
            aux.push(self.pop())

        while not aux.esta_vazia():
            self.push(aux.pop())
        return removido

    def remover_repetidos(self):
        vistos = Pilha()
        aux = Pilha()
        while not self.esta_vazia():
            dado = self.pop()
            if not vistos.buscar(dado):
                vistos.push(dado)
                aux.push(dado)

        while not aux.esta_vazia():
            self.push(aux.pop())
        vistos.destruir()