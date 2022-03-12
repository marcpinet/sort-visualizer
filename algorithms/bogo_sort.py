from random import shuffle


def sort(array: list[int]):
    """Bogo Sort"""

    def _is_sorted(a):
        n = len(a)
        for i in range(0, n - 1):
            if a[i] > a[i + 1]:
                return False
        return True
    
    def _get_diff(array1, array2):
        n = len(array1)
        diff = []
        for i in range(0, n):
            if array1[i] != array2[i]:
                diff.append(i)
        return diff

    while not _is_sorted(array):
        tmp = array.copy()
        shuffle(array)
        yield array, _get_diff(array, tmp)
