# Note: This sorting algorithm is not the most suitable for most cases O(n²)
def bubble_sort(array):
    # Loop through array(i)
    for i in range(len(array)):
    # Loop through array again(j-1)
        for j in range(len(array)-1):
            # If the current element(i) is greater than the next one(j + 1), we swap places for each other.
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubble_sort([5, 3, 2, 8, 1, 4]))
