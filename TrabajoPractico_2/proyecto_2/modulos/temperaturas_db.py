# modulos/temperaturas_db.py
from datetime import datetime, date #p convertir fechas escritas en objetos asi se pueden comparar
from typing import Optional, Tuple, List
import csv 
# 
class NodoAVL: #aca cada objeto (nodo del arobol) será entrada con fecha + T
    def __init__(self, fecha: date, temperatura: float): #define el constructor de la clase, self es referencia al objeto q creo y desp los datos q se le pasan al nodo
        self.fecha: date = fecha #guarda el valor de la fecha dentro del nodo, es clave para organizar el arbol (izq o derecha)
        self.temperatura: float = temperatura #guarda valor de la T asociado a la fecha
        self.izq: Optional['NodoAVL'] = None #inicializa puntero, apunta a los nodos con fechas menores a la actual
        self.der: Optional['NodoAVL'] = None #apunta a los nodos con fechas mayores a la actual
        self.altura: int = 1 #guarda ubicacion del nodo en la rama, como lo estamos creando va en 1, esto se va actualizando cuando se agregan o eliminan nodos
    #si hay diferencia de altura  (>1 o <-1) entre izq y derecha, hay q rotar p que quede balanceado 


# 
class Temperaturas_DB: #tiene toda la logica AVL
    def __init__(self): #constructor de la base de datos
        self.raiz: Optional[NodoAVL] = None #guarda la raiz del arbol y metodos, apunta al nodo raiz del arbol, pone none xq inicialmente no hay nodos
        self._cantidad: int = 0 #guarda la cant de mediciones cargadas, empieza en 0, se incrementa al agregar o decrementa al borrar

    # ayudas de AVL 
    def _altura(self, nodo: Optional[NodoAVL]) -> int:
        return nodo.altura if nodo else 0 #si llega a haber un nodo te dice su altura 

    def _balance(self, nodo: Optional[NodoAVL]) -> int:
        return self._altura(nodo.izq) - self._altura(nodo.der) if nodo else 0 #calcula facotr de balance, o sea p saber si es necesario rotar o no. si no hay nodo devuelve 0. si sale >1 o <-1 indica desbalance

    def _rotar_derecha(self, y: NodoAVL) -> NodoAVL: #hace la rotacion a la derecha
        x = y.izq
        T2 = x.der
        x.der = y
        y.izq = T2
        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))
        x.altura = 1 + max(self._altura(x.izq), self._altura(x.der))
        return x

    def _rotar_izquierda(self, x: NodoAVL) -> NodoAVL: #hace la rotacion a la izquierda
        y = x.der
        T2 = y.izq
        y.izq = x
        x.der = T2
        x.altura = 1 + max(self._altura(x.izq), self._altura(x.der))
        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))
        return y

    # ---------- Insertar / actualizar ----------
    def guardar_temperatura(self, temperatura: float, fecha_str: str): #recibe T y fecha como str dd/mm/aaaa
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
    #convierte la cadena a datetime
        self.raiz, inserted = self._insertar(self.raiz, fecha, float(temperatura)) #mete la info
        if inserted:
            self._cantidad += 1 #si es q se metio algo, modifica el contador

    def _insertar(self, nodo: Optional[NodoAVL], fecha: date, temp: float) -> Tuple[Optional[NodoAVL], bool]:
        if nodo is None: #crea un nodo con fecha y temperatura
            return NodoAVL(fecha, temp), True

        if fecha < nodo.fecha: #mete en subarbol izquierdo
            nodo.izq, inserted = self._insertar(nodo.izq, fecha, temp)
        elif fecha > nodo.fecha: #mete en subarbol derecho
            nodo.der, inserted = self._insertar(nodo.der, fecha, temp)
        else:
            # misma fecha: actualizar temperatura (no cambia tamaño)
            nodo.temperatura = temp
            return nodo, False

        nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der)) #actualiza la altura del nodo por lo q se agrego
        balance = self._balance(nodo) #calcula el factor de balance

        # Casos AVL: p donde hay q rotar si hay desbalance
        if balance > 1 and fecha < nodo.izq.fecha:
            return self._rotar_derecha(nodo), inserted
        if balance < -1 and fecha > nodo.der.fecha:
            return self._rotar_izquierda(nodo), inserted
        if balance > 1 and fecha > nodo.izq.fecha:
            nodo.izq = self._rotar_izquierda(nodo.izq)
            return self._rotar_derecha(nodo), inserted
        if balance < -1 and fecha < nodo.der.fecha:
            nodo.der = self._rotar_derecha(nodo.der)
            return self._rotar_izquierda(nodo), inserted

        return nodo, inserted

    # Buscar temperatura exacta
    def devolver_temperatura(self, fecha_str: str) -> Optional[float]:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        nodo = self._buscar(self.raiz, fecha) #llama a buscar
        return nodo.temperatura if nodo else None #si encontro devuelve lo q buscas

    def _buscar(self, nodo: Optional[NodoAVL], fecha: date) -> Optional[NodoAVL]:
        if not nodo:
            return None
        if fecha == nodo.fecha:
            return nodo
        if fecha < nodo.fecha:
            return self._buscar(nodo.izq, fecha)
        return self._buscar(nodo.der, fecha)

    # ---------- Borrar ----------
    def borrar_temperatura(self, fecha_str: str) -> bool:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        deleted, self.raiz = self._borrar(self.raiz, fecha)
        if deleted:
            self._cantidad -= 1
        return deleted

    def _borrar(self, nodo: Optional[NodoAVL], fecha: date) -> Tuple[bool, Optional[NodoAVL]]:
        if nodo is None:
            return False, None

        deleted = False
        if fecha < nodo.fecha:
            deleted, nodo.izq = self._borrar(nodo.izq, fecha)
        elif fecha > nodo.fecha:
            deleted, nodo.der = self._borrar(nodo.der, fecha)
        else:
            # encontrado
            deleted = True
            if nodo.izq is None:
                return True, nodo.der
            elif nodo.der is None:
                return True, nodo.izq
            else:
                # dos hijos: usar sucesor (mínimo en subárbol derecho)
                sucesor = self._min_nodo(nodo.der)
                nodo.fecha = sucesor.fecha
                nodo.temperatura = sucesor.temperatura
                # borrar el sucesor (solo uno se eliminará físicamente en la recursión)
                _, nodo.der = self._borrar(nodo.der, sucesor.fecha)

        if nodo is None:
            return deleted, None

        # actualizar y rebalancear
        nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))
        balance = self._balance(nodo)

        if balance > 1 and self._balance(nodo.izq) >= 0:
            return deleted, self._rotar_derecha(nodo)
        if balance > 1 and self._balance(nodo.izq) < 0:
            nodo.izq = self._rotar_izquierda(nodo.izq)
            return deleted, self._rotar_derecha(nodo)
        if balance < -1 and self._balance(nodo.der) <= 0:
            return deleted, self._rotar_izquierda(nodo)
        if balance < -1 and self._balance(nodo.der) > 0:
            nodo.der = self._rotar_derecha(nodo.der)
            return deleted, self._rotar_izquierda(nodo)

        return deleted, nodo

    def _min_nodo(self, nodo: NodoAVL) -> NodoAVL:
        current = nodo
        while current.izq:
            current = current.izq
        return current

    # ---------- Consultas por rango (devuelven tuplas internas) ----------
    def _rango(self, nodo: Optional[NodoAVL], f1: date, f2: date, salida: List[Tuple[date, float]]):
        if not nodo:
            return
        # si hay posibilidad de que el subárbol izquierdo contenga fechas >= f1
        if nodo.fecha > f1:
            self._rango(nodo.izq, f1, f2, salida)
        if f1 <= nodo.fecha <= f2:
            salida.append((nodo.fecha, nodo.temperatura))
        # si hay posibilidad de que el subárbol derecho contenga fechas <= f2
        if nodo.fecha < f2:
            self._rango(nodo.der, f1, f2, salida)

    def devolver_temperaturas(self, fecha1: str, fecha2: str) -> List[str]:
        f1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        f2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        if f1 > f2:
            raise ValueError("fecha1 debe ser <= fecha2")
        tuplas: List[Tuple[date, float]] = []
        self._rango(self.raiz, f1, f2, tuplas)   # ya salen ordenadas
        return [f"{f.strftime("%Y-%m-%d")}: {t} ºC" for f, t in tuplas]

    def max_temp_rango(self, fecha1: str, fecha2: str) -> Optional[float]:
        f1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        f2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        if f1 > f2:
            raise ValueError("fecha1 debe ser <= fecha2")
        tuplas: List[Tuple[date, float]] = []
        self._rango(self.raiz, f1, f2, tuplas)
        if not tuplas:
            return None
        maxv = tuplas[0][1]
        for _, t in tuplas:
            if t > maxv:
                maxv = t
        return maxv

    def min_temp_rango(self, fecha1: str, fecha2: str) -> Optional[float]:
        f1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        f2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        if f1 > f2:
            raise ValueError("fecha1 debe ser <= fecha2")
        tuplas: List[Tuple[date, float]] = []
        self._rango(self.raiz, f1, f2, tuplas)
        if not tuplas:
            return None
        minv = tuplas[0][1]
        for _, t in tuplas:
            if t < minv:
                minv = t
        return minv

    def temp_extremos_rango(self, fecha1: str, fecha2: str) -> Tuple[Optional[float], Optional[float]]:
        # calculamos min y max en una sola pasada (más eficiente que llamar a min y max por separado)
        f1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
        f2 = datetime.strptime(fecha2, "%Y-%m-%d").date()
        if f1 > f2:
            raise ValueError("fecha1 debe ser <= fecha2")
        tuplas: List[Tuple[date, float]] = []
        self._rango(self.raiz, f1, f2, tuplas)
        if not tuplas:
            return (None, None)
        minv = maxv = tuplas[0][1]
        for _, t in tuplas:
            if t < minv:
                minv = t
            if t > maxv:
                maxv = t
        return (minv, maxv)

    def cantidad_muestras(self) -> int:
        return self._cantidad

    # ---------- Método para cargar desde archivo ----------
    def cargar_desde_archivo(self, ruta_archivo: str, saltar_encabezado: bool = True):
        """
        Lee líneas del archivo y guarda las temperaturas.
        Admite líneas:
            dd/mm/yyyy;temperatura
            dd/mm/yyyy;HH:MM;temperatura
        Si hay encabezado (cabeceras), pasar saltar_encabezado=True para intentar ignorarla.
        """
        with open("data/muestras.txt", "r", encoding="utf-8") as f:

            lineas = f.readlines()

        for i, linea in enumerate(lineas):
            linea = linea.strip()
            if not linea:
                continue
            partes = [p.strip() for p in linea.split(";") if p.strip() != ""]
            # intentar detectar y saltar encabezado simple
            if saltar_encabezado and i == 0:
                # si la primera parte no es parseable como fecha, saltar
                try:
                    datetime.strptime(partes[0], "%Y-%m-%d")
                except Exception:
                    continue
            try:
                if len(partes) == 2:
                    fecha_txt, temp_txt = partes
                elif len(partes) >= 3:
                    # si hay hora en el medio, la temperatura suele ser el último campo
                    fecha_txt, temp_txt = partes[0], partes[-1]
                else:
                    continue
                temp = float(temp_txt)
                # validar fecha formateada
                datetime.strptime(fecha_txt, "%Y-%m-%d")
                self.guardar_temperatura(temp, fecha_txt)
            except Exception:
                # línea malformada -> ignorar
                continue






   
