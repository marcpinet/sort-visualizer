def sort(array: list[int], low: int = 0, length: int = 0, direction: int = 1):
    if length == 0:
        length = len(array)
    
    def _comp_and_swap(array: list[int], index1: int, index2: int, direction: int):
        if (direction == 1 and array[index1] > array[index2]) or (
            direction == 0 and array[index1] < array[index2]
        ):
            array[index1], array[index2] = array[index2], array[index1]
            yield array, [array[index1], array[index2]]


    def _bitonic_merge(array: list[int], low: int, length: int, direction: int):
        if length > 1:
            middle = int(length / 2)
            for i in range(low, low + middle):
                yield from _comp_and_swap(array, i, i + middle, direction)
            yield from _bitonic_merge(array, low, middle, direction)
            yield from _bitonic_merge(array, low + middle, middle, direction)
    
    if length > 1:
        middle = int(length / 2)
        yield from sort(array, low, middle, 1)
        yield from sort(array, low + middle, middle, 0)
        yield from _bitonic_merge(array, low, length, direction)
    
    yield array, []