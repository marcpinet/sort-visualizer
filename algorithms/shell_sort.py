def sort(array: list[int]):
    """Shell Sort"""
    
    interval = len(array) // 2
    while interval > 0:
        for i in range(interval, len(array)):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
                yield array, [array[i], array[j]]
            array[j] = temp
            yield array, [array[i], array[j]]
        interval //= 2
        yield array, [-1]
