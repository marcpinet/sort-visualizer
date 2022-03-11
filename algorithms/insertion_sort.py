import time

def sort(array: list[int]):
    """Insertion Sort"""
    start_time = time.time()
    
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
            yield array, [array[i], array[j]], time.time() - start_time
        array[i + 1] = key
        
        yield array, [array[i], array[j]], time.time() - start_time