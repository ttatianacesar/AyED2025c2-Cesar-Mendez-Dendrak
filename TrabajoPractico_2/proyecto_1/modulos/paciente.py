from random import randint, choices
import time 

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:  
    
    def __init__(self):
        n = len(nombres)  #8
        self.__nombre = nombres[randint(0, n-1)]  #entre 0 y 7
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0] #toma solo el valor, un entero
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1] #acceder al indice de descripciones de riesgo con el valor del riesgo
        self.__tiempo_llegada= time.time()
        

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def get_tiempo_llegada(self):
        return self.__tiempo_llegada
    
    def __str__(self):
        cad = self.__nombre + ' ' 
        cad += self.__apellido  + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        return cad

    
    def __lt__(self, otro):
        if self.__riesgo == otro.__riesgo:
            return self.__tiempo_llegada < otro.__tiempo_llegada
        return self.__riesgo < otro.__riesgo   #bien

    def __eq__(self, otro):
        return self.__riesgo == otro.__riesgo and self.__tiempo_llegada == otro.__tiempo_llegada
       

