# Algoritmos de ordenamiento
# -------------------------
import random
import time
import matplotlib.pyplot as plt
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # dígitos 0-9

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = n-1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index]-1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

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

# -------------------------
# Ejecutar pruebas
# -------------------------
tamaños = list(range(1, 1001))
tiempos_burbuja = []
tiempos_quick = []
tiempos_radix = []
tiempos_sorted = []

print("Midiendo tiempos, esto puede tardar un poco...")

for n in tamaños:
    lst = generar_lista(n)
    tiempos_burbuja.append(medir_tiempo(bubble_sort, lst))
    tiempos_quick.append(medir_tiempo(quicksort, lst))
    tiempos_radix.append(medir_tiempo(radix_sort, lst))
    tiempos_sorted.append(medir_tiempo(sorted, lst))

# -------------------------
# Graficar resultados
# -------------------------
plt.figure(figsize=(12,6))
plt.plot(tamaños, tiempos_burbuja, label='Bubble Sort')
plt.plot(tamaños, tiempos_quick, label='QuickSort')
plt.plot(tamaños, tiempos_radix, label='Radix Sort')
plt.plot(tamaños, tiempos_sorted, label='Python sorted')
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (s)")
plt.title("Comparación de algoritmos de ordenamiento")
plt.legend()
plt.grid(True)
plt.show()

# -------------------------
# Complejidad a priori
# -------------------------
print("\nComplejidades teóricas:")
print("Bubble Sort: O(n^2)")
print("QuickSort: O(n log n) promedio, O(n^2) peor caso")
print("Radix Sort: O(d·n), d = número de dígitos")
print("Python sorted (Timsort): O(n log n) en el peor caso")
