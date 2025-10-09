
#ACA ABAJO VA EL NUEVO: Esta clase crea internamente un objeto del tipo ArbolAVL.
#Sus métodos llaman a las funciones del árbol para guardar, obtener o eliminar datos. Es como la BD de mi amigo Kevinp

from datetime import datetime
from modulos.arbol_avl import ArbolAVL

class Temperaturas_DB:
    def __init__(self):
        # Crear el árbol AVL vacío
        self.arbol = ArbolAVL()

    # --- Operaciones básicas ---

    def guardar_temperatura(self, temperatura, fecha):
        """Guarda la temperatura asociada a una fecha."""
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y").date()
        self.arbol.agregar(fecha_dt, temperatura)

    def devolver_temperatura(self, fecha):
        """Devuelve la temperatura registrada en una fecha."""
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y").date()
        return self.arbol.obtener(fecha_dt)

    def borrar_temperatura(self, fecha):
        """Elimina la medición asociada a una fecha."""
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y").date()
        self.arbol.eliminar(fecha_dt)

    def cantidad_muestras(self):
        """Devuelve la cantidad total de registros."""
        return self.arbol.tamano

    # --- Consultas por rango ---

    def devolver_temperaturas(self, fecha1, fecha2):
        """Devuelve una lista de mediciones entre dos fechas (inclusive)."""
        f1 = datetime.strptime(fecha1, "%d/%m/%Y").date()
        f2 = datetime.strptime(fecha2, "%d/%m/%Y").date()
        resultados = []
        self._inorden_rango(self.arbol.raiz, f1, f2, resultados)
        return resultados

    def _inorden_rango(self, nodo, f1, f2, resultados):
        """Recorrido inorden que agrega las fechas dentro del rango."""
        if nodo is None:
            return
        if nodo.clave > f1:
            self._inorden_rango(nodo.hijoIzquierdo, f1, f2, resultados)
        if f1 <= nodo.clave <= f2:
            resultados.append(f"{nodo.clave.strftime('%d/%m/%Y')}: {nodo.cargaUtil} ºC")
        if nodo.clave < f2:
            self._inorden_rango(nodo.hijoDerecho, f1, f2, resultados)

    def max_temp_rango(self, fecha1, fecha2):
        """Devuelve la temperatura máxima en el rango."""
        lista = self.devolver_temperaturas(fecha1, fecha2)
        if not lista:
            return None
        temps = [float(s.split(": ")[1].split(" ")[0]) for s in lista]
        return max(temps)

    def min_temp_rango(self, fecha1, fecha2):
        """Devuelve la temperatura mínima en el rango."""
        lista = self.devolver_temperaturas(fecha1, fecha2)
        if not lista:
            return None
        temps = [float(s.split(": ")[1].split(" ")[0]) for s in lista]
        return min(temps)

    def temp_extremos_rango(self, fecha1, fecha2):
        """Devuelve (mínimo, máximo) en el rango."""
        lista = self.devolver_temperaturas(fecha1, fecha2)
        if not lista:
            return None, None
        temps = [float(s.split(": ")[1].split(" ")[0]) for s in lista]
        return min(temps), max(temps)

#PARA LEER ARCHIVO MUESTRAS.TXT:
    def cargar_desde_archivo(self, nombre_archivo):
        """Lee un archivo de muestras y carga las temperaturas en la base de datos."""
        try:
            with open(nombre_archivo, "r", encoding="utf-16") as archivo: #sino no abre x tipo archivo
                for linea in archivo:
                    linea = linea.strip()
                    if not linea:
                        continue
                    partes = linea.split(";")
                    if len(partes) != 2:
                        continue
                    fecha_iso, temp_str = partes
                    # Convertir fecha de 'aaaa-mm-dd' a 'dd/mm/aaaa' para usar internamente
                    fecha = datetime.strptime(fecha_iso, "%Y-%m-%d").strftime("%d/%m/%Y")
                    temperatura = float(temp_str)
                    self.guardar_temperatura(temperatura, fecha)
            print("Muestras cargadas correctamente.")
        except FileNotFoundError:
            print(f"No se encontró el archivo '{nombre_archivo}'.")
        except Exception as e:
            print("Error al leer el archivo:", e)
#Abre el archivo línea por línea, Divide cada línea por ;
#Convierte la fecha al formato "dd/mm/aaaa" que usa tu base. Convierte la temperatura a float
#Llama a guardar_temperatura para insertar en el árbol AVL