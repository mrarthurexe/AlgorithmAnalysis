# Note: O(n²)
def insertion_sort(array):
  for i in range(1, len(array)):
    # Key the value of the current element given position(i)
    key_value = array[i]

    # We store the index we are currently pointing to
    pointed_index = i

    # In case the pointed index is greater than zero and the previous position value is greater than the key value, then:
    while pointed_index > 0 and array[pointed_index - 1] > key_value:
      # Sets the value contained in the pointed position to the value of the previous position.
      array[pointed_index] = array[pointed_index - 1]
      # Goes back one position in the array to compare with the next previous value
      pointed_index -= 1
      
    # Stores the key value at the pointed position at the moment, since if the previous "while" is not started,
    # it means that the element is in the correct position
    array[pointed_index] = key_value
    
  return array
print(insertion_sort([5, 2, 4, 6, 1, 3]))