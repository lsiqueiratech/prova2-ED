from node import Node

class Fila():

    def __init__(self):
        self.inicio = None
        self.final = None

    def esta_vazia(self):
        return not self.inicio

    def enqueue(self,dado):
        novo = Node(dado)
        if not self.esta_vazia():
            self.final.prox = novo
            self.final = novo
        else:
            self.inicio = novo
            self.final = novo

    def dequeue(self):
        aux = self.inicio
        if not self.esta_vazia():
            if self.inicio != self.final:
                self.inicio = self.inicio.prox
            else:
                self.inicio = None
                self.final = None
            dado = aux.item
            del aux
            return dado

    def first(self):
        if not self.esta_vazia():
            return self.inicio.item

    def destruir(self):
        while not self.esta_vazia():
            self.dequeue()

    def imprimir(self):
        aux = Fila()
        while not self.esta_vazia():
            print(self.first())
            aux.enqueue(self.dequeue())

        while not aux.esta_vazia():
            self.enqueue(aux.dequeue())

    def imprimir_fila(self):
        aux = Fila()
        while not self.esta_vazia():
            dado = self.dequeue()
            print(dado)
            aux.enqueue(dado)

        while not aux.esta_vazia():
            self.enqueue(aux.dequeue())

    def buscar(self, info):
        aux = Fila()
        achou = False
        while not self.esta_vazia():
            dado = self.dequeue()
            if dado == info:
                achou = True
            aux.enqueue(dado)

        while not aux.esta_vazia():
            self.enqueue(aux.dequeue())
        return achou

    def editar(self, info, novo_valor):
        aux = Fila()
        editado = False
        while not self.esta_vazia():
            dado = self.dequeue()
            if not editado and dado == info:
                dado = novo_valor
                editado = True
            aux.enqueue(dado)

        while not aux.esta_vazia():
            self.enqueue(aux.dequeue())
        return editado

    def remover(self, info):
        aux = Fila()
        removido = False
        while not self.esta_vazia():
            dado = self.dequeue()
            if not removido and dado == info:
                removido = True
            else:
                aux.enqueue(dado)

        while not aux.esta_vazia():
            self.enqueue(aux.dequeue())
        return removido

    def remover_repetidos(self):
        vistos = Fila()
        aux = Fila()
        while not self.esta_vazia():
            dado = self.dequeue()
            if not vistos.buscar(dado):
                vistos.enqueue(dado)
                aux.enqueue(dado)

        while not aux.esta_vazia():
            self.enqueue(aux.dequeue())
        vistos.destruir()