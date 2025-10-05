from datetime import datetime

# ---------- Nodo del AVL ----------
class NodoAVL:
    def __init__(self, fecha, temperatura):
        self.fecha = fecha
        self.temperatura = temperatura
        self.izq = None
        self.der = None
        self.altura = 1


# ---------- Clase Temperaturas_DB ----------
class Temperaturas_DB:
    def __init__(self):
        self.raiz = None
        self._cantidad = 0

    # ----- Utilidades internas -----
    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def _balance(self, nodo):
        return self._altura(nodo.izq) - self._altura(nodo.der) if nodo else 0

    def _rotar_derecha(self, y):
        x = y.izq
        T2 = x.der
        x.der = y
        y.izq = T2
        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))
        x.altura = 1 + max(self._altura(x.izq), self._altura(x.der))
        return x

    def _rotar_izquierda(self, x):
        y = x.der
        T2 = y.izq
        y.izq = x
        x.der = T2
        x.altura = 1 + max(self._altura(x.izq), self._altura(x.der))
        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))
        return y

    # ----- Insertar nodo -----
    def guardar_temperatura(self, temperatura, fecha):
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        self.raiz = self._insertar(self.raiz, fecha_dt, temperatura)

    def _insertar(self, nodo, fecha, temp):
        if not nodo:
            self._cantidad += 1
            return NodoAVL(fecha, temp)
        if fecha < nodo.fecha:
            nodo.izq = self._insertar(nodo.izq, fecha, temp)
        elif fecha > nodo.fecha:
            nodo.der = self._insertar(nodo.der, fecha, temp)
        else:
            nodo.temperatura = temp
            return nodo

        nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))
        balance = self._balance(nodo)

        # Rotaciones
        if balance > 1 and fecha < nodo.izq.fecha:
            return self._rotar_derecha(nodo)
        if balance < -1 and fecha > nodo.der.fecha:
            return self._rotar_izquierda(nodo)
        if balance > 1 and fecha > nodo.izq.fecha:
            nodo.izq = self._rotar_izquierda(nodo.izq)
            return self._rotar_derecha(nodo)
        if balance < -1 and fecha < nodo.der.fecha:
            nodo.der = self._rotar_derecha(nodo.der)
            return self._rotar_izquierda(nodo)

        return nodo

    # ----- Buscar temperatura -----
    def devolver_temperatura(self, fecha):
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        nodo = self._buscar(self.raiz, fecha_dt)
        return nodo.temperatura if nodo else None

    def _buscar(self, nodo, fecha):
        if not nodo:
            return None
        if fecha == nodo.fecha:
            return nodo
        if fecha < nodo.fecha:
            return self._buscar(nodo.izq, fecha)
        else:
            return self._buscar(nodo.der, fecha)

    # ----- Borrar temperatura -----
    def borrar_temperatura(self, fecha):
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        self.raiz = self._borrar(self.raiz, fecha_dt)

    def _borrar(self, nodo, fecha):
        if not nodo:
            return None
        if fecha < nodo.fecha:
            nodo.izq = self._borrar(nodo.izq, fecha)
        elif fecha > nodo.fecha:
            nodo.der = self._borrar(nodo.der, fecha)
        else:
            self._cantidad -= 1
            if not nodo.izq:
                return nodo.der
            elif not nodo.der:
                return nodo.izq
            temp = self._min_nodo(nodo.der)
            nodo.fecha, nodo.temperatura = temp.fecha, temp.temperatura
            nodo.der = self._borrar(nodo.der, temp.fecha)

        nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))
        balance = self._balance(nodo)

        # Rebalanceo
        if balance > 1 and self._balance(nodo.izq) >= 0:
            return self._rotar_derecha(nodo)
        if balance > 1 and self._balance(nodo.izq) < 0:
            nodo.izq = self._rotar_izquierda(nodo.izq)
            return self._rotar_derecha(nodo)
        if balance < -1 and self._balance(nodo.der) <= 0:
            return self._rotar_izquierda(nodo)
        if balance < -1 and self._balance(nodo.der) > 0:
            nodo.der = self._rotar_derecha(nodo.der)
            return self._rotar_izquierda(nodo)
        return nodo

    def _min_nodo(self, nodo):
        while nodo.izq:
            nodo = nodo.izq
        return nodo

    # ----- Consultas en rango -----
    def _rango(self, nodo, f1, f2, lista):
        if not nodo:
            return
        if nodo.fecha > f1:
            self._rango(nodo.izq, f1, f2, lista)
        if f1 <= nodo.fecha <= f2:
            lista.append((nodo.fecha, nodo.temperatura))
        if nodo.fecha < f2:
            self._rango(nodo.der, f1, f2, lista)

    def devolver_temperaturas(self, fecha1, fecha2):
        f1 = datetime.strptime(fecha1, "%d/%m/%Y")
        f2 = datetime.strptime(fecha2, "%d/%m/%Y")
        lista = []
        self._rango(self.raiz, f1, f2, lista)
        lista.sort()
        return [f"{f.strftime('%d/%m/%Y')}: {t} ºC" for f, t in lista]

    def max_temp_rango(self, fecha1, fecha2):
        temps = self.devolver_temperaturas(fecha1, fecha2)
        if not temps:
            return None
        return max([float(t.split(': ')[1].split()[0]) for t in temps])

    def min_temp_rango(self, fecha1, fecha2):
        temps = self.devolver_temperaturas(fecha1, fecha2)
        if not temps:
            return None
        return min([float(t.split(': ')[1].split()[0]) for t in temps])

    def temp_extremos_rango(self, fecha1, fecha2):
        return (self.min_temp_rango(fecha1, fecha2),
                self.max_temp_rango(fecha1, fecha2))

    def cantidad_muestras(self):
        return self._cantidad

    # ----- Cargar desde archivo -----
    def cargar_desde_archivo(self, archivo):
        with open(archivo, "r") as f:
            for linea in f:
                if linea.strip():
                    fecha, temp = linea.strip().split(',')
                    self.guardar_temperatura(float(temp), fecha)
class BaseDeDatosTemperaturas:
    def __init__(self):
        self.registros = []  # acá se guardan las muestras cargadas

    def cargar_desde_archivo(self, ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        for linea in lineas[1:]:  # saltea la primera línea si tiene encabezado
            partes = linea.strip().split(",")  # o usa ";" si el archivo tiene punto y coma
            if len(partes) >= 3:
                fecha = partes[0]
                hora = partes[1]
                temperatura = float(partes[2])
                self.registros.append((fecha, hora, temperatura))

    def mostrar_registros(self):
        for r in self.registros:
            print(r)
