def sort(array: list[int]):
    """Shell Sort"""
    
    interval = len(array) // 2
    while interval > 0:
        for i in range(interval, len(array)):
            passed = False
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                passed = True
                array[j] = array[j - interval]
                j -= interval
                yield array, [array[i], array[j]]
            array[j] = temp
            if not passed:
                yield array, [array[i], array[j]]
        interval //= 2
        yield array, []
