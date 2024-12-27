class Pilha:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

class Fila:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

class Lista:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

pilha = Pilha()
fila = Fila()
lista = Lista()
