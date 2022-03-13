def sort(array: list[int]):
    is_sorted = False
    while not is_sorted:  # Until all the indices are traversed keep looping
        is_sorted = True
        passed = False
        for i in range(0, len(array) - 1, 2):  # iterating over all even indices
            if array[i] > array[i + 1]:

                array[i], array[i + 1] = array[i + 1], array[i]
                yield array, [array[i], array[i + 1]]
                passed = True
                # swapping if elements not in order
                is_sorted = False
            if not passed:
                yield array, [array[i], array[i + 1]]

        for i in range(1, len(array) - 1, 2):  # iterating over all odd indices
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                passed = True
                yield array, [array[i], array[i + 1]]
                # swapping if elements not in order
                is_sorted = False
            if not passed:
                yield array, [array[i], array[i + 1]]

    yield array, []
