def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

#----prueba unitaria---
if __name__ == "__main__":
    import random

    print("\n=== PRUEBAS: QUICKSORT ===")

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
        resultado = quicksort(lista.copy())
        print(f"Prueba {i}: {'OK' if resultado == sorted(lista) else 'FALLO'}")