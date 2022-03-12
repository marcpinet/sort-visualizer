def sort(array: list[int]):
    """Insertion Sort"""
    
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
            yield array, [array[i], array[j]]
        array[i + 1] = key
        
        yield array, [array[i], array[j]]