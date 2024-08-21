import threading

class MergeSortThread(threading.Thread):
    def __init__(self, array):
        threading.Thread.__init__(self)
        self.array = array
        self.sorted_array = []

    def run(self):
        if len(self.array) <= 1:
            self.sorted_array = self.array
        else:
            media = len(self.array) // 2
            array1 = self.array[:media]
            array2 = self.array[media:]

            # Crear hilos para ordenar ambas mitades
            thread1 = MergeSortThread(array1)
            thread2 = MergeSortThread(array2)

            # Iniciar los hilos
            thread1.start()
            thread2.start()

            # Esperar a que ambos hilos terminen
            thread1.join()
            thread2.join()

            # Fusionar los resultados
            self.sorted_array = merge(thread1.sorted_array, thread2.sorted_array)

def merge(array1, array2):
    ordered_array = []
    i = j = 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            ordered_array.append(array1[i])
            i += 1
        else:
            ordered_array.append(array2[j])
            j += 1
    
    ordered_array.extend(array1[i:])
    ordered_array.extend(array2[j:])
    
    return ordered_array

# Array original a ordenar
original_array = [2, 1, 4, 23, 9, 1, 1, 3, 6, 5, 9, 12, 11]

# Crear y ejecutar el hilo de ordenamiento
merge_sort_thread = MergeSortThread(original_array)
merge_sort_thread.start()
merge_sort_thread.join()

# Obtener el array ordenado
ordered_array = merge_sort_thread.sorted_array

# Imprimir el array ordenado
print(ordered_array)
