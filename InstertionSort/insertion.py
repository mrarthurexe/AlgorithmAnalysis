ordenar = [5, 4, 2, 4, 1, 3]
x = 10
def insertionSort(array):
    
    for i in range(1, len(array)):
        chave = array[i]
        j = i - 1
        
        #Utilizamos a chave sendo a respectiva posição no array.
        #Comparamos a chave com cada elemento da esquerda, que é representado por "j", sendo a posição atual -1. 
        
        while j >= 0 and chave < array[j]:
            #Quando a chave for menor, j + 1 que será a posição da chave, é substituida pelo valor de [j]
            array[j + 1] = array[j]
            j = j - 1
        
        # Aqui j + 1 receberá o valor da chave, que se for menor, irá para a posição atual do array[j]
        array[j + 1] = chave

insertionSort(ordenar)
print('Lista ordenada:')
print(ordenar)
