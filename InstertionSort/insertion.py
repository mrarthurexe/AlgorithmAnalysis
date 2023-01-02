def insertion_sort(array):
  for i in range(1, len(array)):
    # Colocamos como chave o valor do elemento atual dada a posição(i)
    valor_chave = array[i]

    # Armazenamos o índice ao qual estaremos apontando no momento
    current_index = i

    # No caso do índice apontado ser maior que zero e o valor da posição anterior for maior que o valor da chave, então:
    while current_index > 0 and array[current_index - 1] > valor_chave:
      # Define o valor contido na posição apontada como sendo o valor da posição anterior.
      array[current_index] = array[current_index - 1]
      # Volta uma posição no array para comparar com o próximo valor anterior
      current_index -= 1
      
    # Armazena o valor chave na posição apontada no momento, já que se o while anterior não for iniciado,
    # quer dizer que o elemento está na posição correta.
    array[current_index] = valor_chave
    
  return array
print(insertion_sort([5, 2, 4, 6, 1, 3]))