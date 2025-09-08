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
        
        if posicion is None or posicion == self.tamanio -1:  #eliminar el ultimo nodo
            dato = self.cola.dato 
            if self.tamanio == 1:       #si solo tiene un nodo
                self.cabeza = self.cola = None
            else:                        #si tiene mas de un nodo
                self.cola = self.cola.anterior 
                self.cola.siguiente = None
            self.tamanio -= 1
            return dato
        
        elif posicion == 0:     #caso eliminar el primer nodo 
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
            self.tamanio -= 1
            return dato
        
        elif 0 < posicion < self.tamanio -1:   #caso eliminar nodo en posicion intermedia
            nodo_actual = self.cabeza
            for _ in range(posicion):
                nodo_actual = nodo_actual.siguiente
            dato = nodo_actual.dato
            nodo_actual.anterior.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente.anterior = nodo_actual.anterior
            self.tamanio -= 1
            return dato
        
    def copiar(self):
        copia_lista= ListaDobleEnlazada()
        for dato in self:
            copia_lista.agregar_al_final(dato)
        return copia_lista
    
    def invertir(self):
        lista_invertida= ListaDobleEnlazada()
        for dato in self:
            lista_invertida.agregar_al_inicio(dato)
        return lista_invertida
    
    def concatenar(self, nueva_lista):
        otra_lista= nueva_lista.copia()
        for dato in nueva_lista:
            otra_lista.agregar_al_final(dato)
        return otra_lista
    
    def len(self):
        return self.tamanio
    
    def __add__(self, otra_lista):
        nueva_lista= self.copiar()
        for dato in otra_lista:
            nueva_lista.agregar_al_final(dato)
        return nueva_lista
    
    def __iter__(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            yield nodo_actual.dato
            nodo_actual = nodo_actual.siguiente

        







