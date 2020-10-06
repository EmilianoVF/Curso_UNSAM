
#%%
class Canguro:

    def __init__(self, nombre):
        self.nombre = nombre
        self.contenido_marsupio = []

    def __str__(self):
        t = [self.nombre + ' tiene en su marsupio:']
        for item in self.contenido_marsupio:
            if hasattr(item, 'nombre'):
                nombre_objeto = "'Otra clase llamada:' " + getattr(item, 'nombre')
                t.append(nombre_objeto)
            else:
                t.append(object.__str__(item))
        return '\n'.join(t)

    def meter_en_marsupio(self, item):

        self.contenido_marsupio.append(item)


madre_canguro = Canguro('Madre')
cangurito = Canguro('cangurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
cangurito.meter_en_marsupio('Dulce de leche')
cangurito.meter_en_marsupio('Chocolate')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)
print(cangurito)

#%%

# canguro_malo.py
"""Este código continene un
bug importante y dificil de ver
"""

class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        if contenido:
            self.contenido_marsupio = contenido  # Ahora anda bien
        else:
            self.contenido_marsupio = []

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

madre_canguro = Canguro('Madre')
cangurito = Canguro('cangurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
cangurito.meter_en_marsupio('Dulce de leche')
cangurito.meter_en_marsupio('Chocolate')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)
print(cangurito)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.

