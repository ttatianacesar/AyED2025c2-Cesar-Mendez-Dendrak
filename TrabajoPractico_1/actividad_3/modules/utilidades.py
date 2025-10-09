import random
import time

# -------------------------
# Generar lista aleatoria
# -------------------------
def generar_lista(n):
    return [random.randint(10000, 99999) for _ in range(n)]


# -------------------------
# Medir tiempos
# -------------------------
def medir_tiempo(algoritmo, lista):
    start = time.time()
    algoritmo(lista.copy())
    end = time.time()
    return end - start