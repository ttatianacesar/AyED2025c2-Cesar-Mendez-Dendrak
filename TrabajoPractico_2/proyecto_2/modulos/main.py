from temperaturas import Temperaturas_DB

db = Temperaturas_DB()
db.guardar_temperatura(20.5, "01/01/2023")
db.guardar_temperatura(22.3, "02/01/2023")
db.guardar_temperatura(19.8, "03/01/2023")

print("Temperatura el 02/01/2023:", db.devolver_temperatura("02/01/2023"))
print("Máxima entre 01/01 y 03/01:", db.max_temp_rango("01/01/2023", "03/01/2023"))
print("Mínima entre 01/01 y 03/01:", db.min_temp_rango("01/01/2023", "03/01/2023"))
print("Extremos:", db.temp_extremos_rango("01/01/2023", "03/01/2023"))
print("Listado en rango:", db.devolver_temperaturas("01/01/2023", "03/01/2023"))
print("Cantidad de muestras:", db.cantidad_muestras())

db.borrar_temperatura("02/01/2023")
print("Cantidad tras borrar:", db.cantidad_muestras())

from modulos.temperaturas import BaseDeDatosTemperaturas

# Crear la base
db = BaseDeDatosTemperaturas()

# Cargar las muestras
db.cargar_desde_archivo("proyecto_2/data/muestras.txt")

# Mostrar las primeras
db.mostrar_registros()
