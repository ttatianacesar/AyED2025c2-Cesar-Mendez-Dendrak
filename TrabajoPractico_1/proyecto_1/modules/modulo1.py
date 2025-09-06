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

    def esta_vacia(self):
     return self.tamanio == 0

    
    
    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)      
        if self.esta_vacia():        
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza 
            self.cabeza.anterior = nuevo_nodo   
            self.cabeza = nuevo_nodo        
        self.tamanio += 1     
    

    def agregar_al_final(self, dato):
        nuevo_nodo= Nodo(dato)
        if self.esta_vacia():
            nuevo_nodo = Nodo(dato)
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamanio += 1 


    def insertar(self, dato, posicion=None):

        if posicion is None or posicion == self.tamanio:
            self.agregar_al_final(dato)

        elif posicion == 0:
            self.agregar_al_inicio(dato)

        elif 0 < posicion < self.tamanio:
            nuevo = Nodo(dato)
            nodo_actual = self.cabeza
            for _ in range(posicion):
                nodo_actual = nodo_actual.siguiente
            nodo_anterior = nodo_actual.anterior
            nuevo.anterior = nodo_anterior   #actualiza punteros y esas cosas del nodo nuevo
            nuevo.siguiente = nodo_actual
            nodo_anterior.siguiente = nuevo
            nodo_actual.anterior = nuevo
            self.tamanio += 1

        else:
            raise IndexError("La posicion esta fuera del rango")

    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise IndexError("La lista esta vacia, no se puede extraer")
        
        if posicion is None or posicion == self.tamanio -1:
            dato = self.cola.dato 
            if self.tamanio == 1:
                self.cabeza = self.cola = None
            else:
                self.cola = self.cola.anterior
                self.cola.siguiente = None
            self.tamanio -= 1
            return dato
        
        elif posicion == 0:
            dato = self.cabeza.dato
        

































    def len(self):
        return self.tamanio






