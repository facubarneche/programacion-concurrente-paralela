def merge_sort(array):
    # Si el array tiene un solo elemento o está vacío, ya está ordenado
    if len(array) <= 1:
        return array
    
    # Encuentra el punto medio y divide el array en dos mitades
    media = len(array) // 2
    array1 = array[:media]
    array2 = array[media:]
    
    # Llama recursivamente a merge_sort en ambas mitades
    array1 = merge_sort(array1)
    array2 = merge_sort(array2)
    
    # Fusión de las mitades ordenadas
    return merge(array1, array2)

def merge(array1, array2):
    ordered_array = []
    i = j = 0
    
    # Compara los elementos de ambos arrays y los agrega en orden
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            ordered_array.append(array1[i])
            i += 1
        else:
            ordered_array.append(array2[j])
            j += 1
    # Añade los elementos restantes de array1 o array2
    ordered_array.extend(array1[i:])
    ordered_array.extend(array2[j:])
    
    return ordered_array

# Array original a ordenar
original_array = [2, 1, 4, 23, 9, 1, 1, 3, 6, 5, 9, 12, 11]

# Llama a la función merge_sort y guarda el resultado
ordered_array = merge_sort(original_array)

# Imprime el array ordenado
print(ordered_array)
