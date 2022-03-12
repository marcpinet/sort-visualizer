import time


def sort(array: list[int]):
    """Bad Sort"""
    start_time = time.time()
    
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
                yield array, [array[min_index]], time.time() - start_time
            else:
                yield array, [array[j]], time.time() - start_time
        array[i], array[min_index] = array[min_index], array[i]
        yield array, [array[i], array[min_index]], time.time() - start_time
    
    yield array, [-1], time.time() - start_time