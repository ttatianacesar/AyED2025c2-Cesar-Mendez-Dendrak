from modulos.temperaturas_db import Temperaturas_DB
import os

def ruta_muestras():
    base = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base, "data", "muestras.txt")

def main():
    db = Temperaturas_DB()

    ruta = ruta_muestras()
    if os.path.exists(ruta):
        print(f"\n Cargando muestras desde: {ruta}")
        db.cargar_desde_archivo(ruta)
    else:
        print(" No se encontró el archivo de muestras, cargando ejemplos manuales...")
        db.guardar_temperatura(20.5, "2025-01-01")
        db.guardar_temperatura(21.0, "2025-01-02")
        db.guardar_temperatura(19.8, "2025-01-03")

    print("\n Muestras cargadas correctamente.")
    print("Cantidad total de muestras:", db.cantidad_muestras())

    print("\nTemperaturas del 2025-01-05 al 2025-01-25:")
    lista = db.devolver_temperaturas("2025-01-05", "2025-01-25")
    for item in lista:
        print(item)

    print("\nTemperatura mínima:", db.min_temp_rango("2025-01-05", "2025-01-25"))
    print("Temperatura máxima:", db.max_temp_rango("2025-01-05", "2025-01-25"))
    print("Extremos (mín, máx):", db.temp_extremos_rango("2025-01-05", "2025-01-25"))

    print("\nTemperatura del 2025-01-10:", db.devolver_temperatura("2025-01-10"))

    print("\nEliminando temperatura del 2025-01-10...")
    borrado = db.borrar_temperatura("2025-01-10")
    print("Resultado:", "Eliminado" if borrado else "No se encontró la fecha")
    print("Cantidad tras borrar:", db.cantidad_muestras())

if __name__ == "__main__":
    main()

