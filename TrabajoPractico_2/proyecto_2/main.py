
from modulos.temperaturas_db import Temperaturas_DB

if __name__ == "__main__":
    bd = Temperaturas_DB()

    # Cargar algunos datos de prueba
    bd.guardar_temperatura(20.5, "01/01/2025")
    bd.guardar_temperatura(21.0, "02/01/2025")
    bd.guardar_temperatura(19.3, "03/01/2025")
    bd.guardar_temperatura(22.7, "04/01/2025")

    print("Cantidad de muestras:", bd.cantidad_muestras())
    print("Temperatura el 02/01:", bd.devolver_temperatura("02/01/2025"))

    print("\nTemperaturas del 01/01 al 03/01:")
    for linea in bd.devolver_temperaturas("01/01/2025", "03/01/2025"):
        print(linea)

    print("\nMáxima en el rango:", bd.max_temp_rango("01/01/2025", "04/01/2025"))
    print("Mínima en el rango:", bd.min_temp_rango("01/01/2025", "04/01/2025"))
    print("Extremos:", bd.temp_extremos_rango("01/01/2025", "04/01/2025"))

#para probar archivo: 
from modulos.temperaturas_db import Temperaturas_DB

if __name__ == "__main__":
    bd = Temperaturas_DB()

    # Intentar cargar desde archivo
    ruta = "data/muestras.txt"  # ajustá según tu carpeta
    bd.cargar_desde_archivo(ruta)

    print("\nCantidad total de muestras:", bd.cantidad_muestras())

    print("\nTemperaturas del 2025-01-10 al 2025-01-15:")
    lista = bd.devolver_temperaturas("10/01/2025", "15/01/2025")
    for linea in lista:
        print(linea)

    print("\nMáxima en el rango:", bd.max_temp_rango("09/01/2025", "29/01/2025"))
    print("Mínima en el rango:", bd.min_temp_rango("09/01/2025", "29/01/2025"))
