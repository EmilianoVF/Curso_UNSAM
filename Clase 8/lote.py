

class Lote:

    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def nombre(self):
        return self.nombre

    def cajones(self):
        return self.cajones

    def precio(self):
        return self.precio

    def costo(self):
        return self.cajones * self.precio

    def vender(self, x):
        self.cajones -= x

    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'
