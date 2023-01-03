# obs: Este algoritmo de ordenação não é o mais adequado para grande parte dos casos O(n²).
def bubble_sort(array):
    # Percorremos o array(i)
    for i in range(len(array)):
    # Percorremos o array novamente(j)
        for j in range(len(array)):
            # Se o elemento atual(i) é maior que o próximo(j + 1), trocamos de lugar um pelo outro.
            if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print(bubble_sort([5, 3, 2, 8, 1, 4]))
