# main.py
from modulos.temperaturas_db import Temperaturas_DB
import os

def ruta_muestras():
    base = os.path.dirname(__file__)   # carpeta del proyecto (donde está main.py)
    return os.path.join(base, "data", "muestras.txt")

def main():
    db = Temperaturas_DB()

    # cargar desde archivo (si existe)
    ruta = ruta_muestras()
    if os.path.exists(ruta):
        print("Cargando muestras desde:", ruta)
        db.cargar_desde_archivo(ruta)
    else:
        print("No se encontró", ruta, "- usando inserciones manuales de ejemplo.")
        db.guardar_temperatura(20.5, "01/01/2023")
        db.guardar_temperatura(22.3, "02/01/2023")
        db.guardar_temperatura(19.8, "03/01/2023")

    print("Cantidad de muestras:", db.cantidad_muestras())
    print("Temperatura 02/01/2023:", db.devolver_temperatura("02/01/2023"))
    print("Listado 01/01/2023-03/01/2023:", db.devolver_temperaturas("01/01/2023", "03/01/2023"))
    print("Mínima en rango:", db.min_temp_rango("01/01/2023", "03/01/2023"))
    print("Máxima en rango:", db.max_temp_rango("01/01/2023", "03/01/2023"))
    print("Extremos:", db.temp_extremos_rango("01/01/2023", "03/01/2023"))

    print("Borro 02/01/2023 ->", db.borrar_temperatura("02/01/2023"))
    print("Cantidad tras borrar:", db.cantidad_muestras())

if __name__ == "__main__":
    main()

from temperaturas_db import Temperaturas_DB

def main():
    bd = Temperaturas_DB()
    bd.cargar_desde_archivo("data/temperaturas.csv")

    print("Cantidad de muestras cargadas:", bd.cantidad_muestras())

    # Ejemplo de consulta
    print("Temperatura del 05/01/2024:", bd.devolver_temperatura("05/01/2024"))

    # Ejemplo de rango
    print("Máxima entre 01/01/2024 y 10/01/2024:", bd.max_temp_rango("01/01/2024", "10/01/2024"))

if __name__ == "__main__":
    main()
