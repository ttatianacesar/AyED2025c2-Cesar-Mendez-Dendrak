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
            self.cabeza = self.cola = nuevo_nodo
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
                raise IndexError("La lista está vacía, no se puede extraer")

            # si no se pasa posición → eliminar último
            if posicion is None:
                posicion = self.tamanio - 1

            # permitir índices negativos
            if posicion < 0:
                posicion = self.tamanio + posicion

            # chequeo de rango después de ajustar el índice
            if posicion < 0 or posicion >= self.tamanio:
                raise IndexError("La posición está fuera de rango")

            # caso eliminar cabeza
            if posicion == 0:
                dato = self.cabeza.dato
                self.cabeza = self.cabeza.siguiente
                if self.cabeza:
                    self.cabeza.anterior = None
                else:
                    self.cola = None  # lista quedó vacía

            # caso eliminar cola
            elif posicion == self.tamanio - 1:
                dato = self.cola.dato
                self.cola = self.cola.anterior
                if self.cola:
                    self.cola.siguiente = None
                else:
                    self.cabeza = None  # lista quedó vacía

            # caso eliminar nodo intermedio
            else:
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
        actual = self.cabeza
        self.cabeza, self.cola = self.cola, self.cabeza  # intercambiamos extremos
        while actual:
            actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
            actual = actual.anterior
    #invierte la misma lista, no crea otra, por lo que dice el enunciado deberia ser asi.
    
    def concatenar(self, otra_lista): #devuelve lista actual con la otra concatenada al final
        for dato in otra_lista:       #la self se modifica y desp devuelve, no deja originales intactas
            self.agregar_al_final(dato)
        return self

    
    def __len__(self):
        return self.tamanio
    
    def __add__(self, otra_lista):
        nueva_lista = self.copiar()       # copiamos self
        nueva_lista.concatenar(otra_lista)  # concatenamos la otra
        return nueva_lista
    #lo cambie para q no modifique las listas originales y devuelva otra

    
    def __iter__(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            yield nodo_actual.dato
            nodo_actual = nodo_actual.siguiente

   
        







