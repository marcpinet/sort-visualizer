def sort(array: list[int]):
    no_of_elements = len(array)
    passed = False
    for i in range(
        0, int(((no_of_elements - 1) / 2) + 1)
    ):  # we don't need to traverse to end of list as
        for j in range(0, no_of_elements - 1):
            if (
                array[j + 1] < array[j]
            ):  # applying bubble sort algorithm from left to right (or forwards)
                temp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = temp
                passed = True
                yield array, [array[j], array[j + 1]]
            if (
                array[no_of_elements - 1 - j] < array[no_of_elements - 2 - j]
            ):  # applying bubble sort algorithm from right to left (or backwards)
                temp = array[no_of_elements - 1 - j]
                array[no_of_elements - 1 - j] = array[no_of_elements - 2 - j]
                array[no_of_elements - 2 - j] = temp
                yield array, [
                    array[no_of_elements - 2 - j],
                    array[no_of_elements - 1 - j],
                ]
                passed = True
            if not passed:
                yield array, [array[i], array[j]]
                passed = False
