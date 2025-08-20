
# creo primero la clase nodo que se va a utlizar en la lista doble
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None 

# creo la lista doble que va a estar inicialmente vacia donde se van a ir agregando los nodos 
class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None 
        self.tamanio = 0
        



