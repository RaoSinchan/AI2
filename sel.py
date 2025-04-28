def selectionSort(array, size):
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            # Select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        (array[ind], array[min_index]) = (array[min_index], array[ind])

# Example usage:
arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
