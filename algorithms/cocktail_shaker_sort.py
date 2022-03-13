def sort(array: list[int]):
    """Cocktail Shaker Sort"""

    n = len(array)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                yield array, [array[i], array[i + 1]]
            
        if not swapped:
            break
        swapped = False
        for i in range(n - 1, 0, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                swapped = True
                yield array, [array[i], array[i - 1]]
            
    yield array, []
