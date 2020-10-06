#%%
class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []
        self.items_con_prioridad = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def encolar_prioridad(self, x):
        self.items_con_prioridad.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')

        if len(self.items_con_prioridad):
            res = self.items_con_prioridad.pop(0)
        else:
            res = self.items.pop(0)
        return res

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return (len(self.items) + len(self.items_con_prioridad)) == 0
     

class TorreDeControl(Cola):
    def __init__(self):
        self.items = []
        self.items_con_prioridad = []

    def nuevo_arribo(self, x):
        self.encolar_prioridad(x)

    def nueva_partida(self, x):
        self.encolar(x)

    def ver_estado(self):
        if (len(self.items) + len(self.items_con_prioridad)) == 0:
            print('No hay vuelos en el aire o en la tierra')
        if len(self.items) != 0:
            item = ', '.join(self.items)
            print('Vuelos esperando para despegar :', item)
        if len(self.items_con_prioridad) != 0:
            item = ', '.join(self.items_con_prioridad)
            print('Vuelos esperando para aterrizar :', item)         

    def asignar_pista(self):
        if self.esta_vacia():
            print('No hay vuelos en espera')
        if len(self.items_con_prioridad):
            vuelo = self.items_con_prioridad[0]
            print('El vuelo', vuelo, 'aterrizo con exito')
            self.desencolar()
            return
        if len(self.items):
            vuelo = self.items[0]
            print('El vuelo', vuelo, 'despego con exito')
            self.desencolar()
            return

