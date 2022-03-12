def sort(array: list[int]):
    """Heap Sort"""

    def heapify(array, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and array[i] < array[l]:
            largest = l
        if r < n and array[largest] < array[r]:
            largest = r
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            yield from heapify(array, n, largest)
        
        yield array, [largest, i]

    n = len(array)
    for i in range(n, -1, -1):
        yield from heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        yield from heapify(array, i, 0)
