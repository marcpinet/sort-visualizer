def sort(array: list[int]):
    """Quick Sort"""

    # A quick sort function that also yields the steps (without using any return statement, only yield)
    def _quick_sort(array: list[int], left: int = None, right: int = None):
        if left is None:
            left = 0
        if right is None:
            right = len(array) - 1

        if left < right:
            pivot = array[right]
            pivot_index = left

            for i in range(left, right):
                if array[i] <= pivot:
                    array[i], array[pivot_index] = array[pivot_index], array[i]
                    pivot_index += 1
                    yield array, [array[i], array[pivot_index - 1]]

            array[pivot_index], array[right] = array[right], array[pivot_index]
            yield array, [array[pivot_index], array[right]]

            yield from _quick_sort(array, left, pivot_index - 1)
            yield from _quick_sort(array, pivot_index + 1, right)

    yield from _quick_sort(array)

    yield array, []
