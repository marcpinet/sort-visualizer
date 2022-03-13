def sort(array: list[int]):
    """Bubble Sort"""
    
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                
                yield array, [array[j], array[j + 1]]
    