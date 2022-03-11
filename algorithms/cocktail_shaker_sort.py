import time


def sort(array: list[int]):
    """Cocktail Shaker Sort"""
    start_time = time.time()

    n = len(array)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                yield array, [array[i], array[i + 1]], time.time() - start_time
            
        if not swapped:
            break
        swapped = False
        for i in range(n - 1, 0, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                swapped = True
                yield array, [array[i], array[i - 1]], time.time() - start_time
            
    end_time = time.time()
    total_time = end_time - start_time
    yield array, [-1], total_time
