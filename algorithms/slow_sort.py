def sort(array: list, start: int = None, end: int = None):
    stop = False
    
    if start is None:
        start = 0

    if end is None:
        end = len(array) - 1
        
    yield array, []

    if start >= end:
        stop = True

    if not stop:
        mid = (start + end) // 2

        yield from sort(array, start, mid)
        yield from sort(array, mid + 1, end)

        if array[end] < array[mid]:
            array[end], array[mid] = array[mid], array[end]
            yield array, [array[end], array[mid]]

        yield from sort(array, start, end - 1)