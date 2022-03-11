import time

def sort(array: list[int]):
    """Selection Sort"""
    start_time = time.time()
    
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        
                yield array, [array[i], array[min_idx]], time.time() - start_time
            
        array[i], array[min_idx] = array[min_idx], array[i]
        
        yield array, [array[i], array[min_idx]], time.time() - start_time