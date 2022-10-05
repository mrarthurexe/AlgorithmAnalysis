from array import array
# Bubble sort algorithm
array = [7, 3, 6, 2, 0]
# Introduzida variável "tamanho" recebendo o tamanho do array.
tamanho = len(array)
# Loop para percorrer o array.
for i in range(tamanho -1):
    # Trocado indica se a posição foi trocada.
    trocado = False
    # For loop percorre "j" que é o tamanho do array - i.
    for j in range (tamanho -i -1):
        #Se o valor de j for maior que o valor de j+1, troca os valores.
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            #Se a condição de troca é confirmada, troca o valor de trocado para True.
            trocado = True
    #Se o valor de trocado for False, o array está ordenado.
    if not trocado:
        break

print(array)
