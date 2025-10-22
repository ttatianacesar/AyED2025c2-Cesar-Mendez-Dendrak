def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


#---prueba unitaria---
if __name__ == "__main__":
    import random

    print("\n=== PRUEBAS: ORDENAMIENTO BURBUJA ===")

    pruebas = [
        [],
        [42],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 1, 2, 3, 1],
        random.sample(range(1, 100), 10),
        [random.randint(10000, 99999) for _ in range(500)]
    ]

    for i, lista in enumerate(pruebas, 1):
        resultado = bubble_sort(lista.copy())
        print(f"Prueba {i}: {'OK' if resultado == sorted(lista) else 'FALLO'}")
