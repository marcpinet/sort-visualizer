def sort(array: list[int]):
    """Bitonic Sort"""

    def _comp_and_swap(a, i, j, dire):
        if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
            a[i], a[j] = a[j], a[i]

    def _bitonic_merge(a, low, cnt, dire):
        if cnt > 1:
            k = cnt // 2
            for i in range(low, low + k):
                _comp_and_swap(a, i, i + k, dire)
            _bitonic_merge(a, low, k, dire)
            _bitonic_merge(a, low + k, k, dire)

    def _bitonic_sort(a, low, cnt, dire):
        if cnt > 1:
            k = cnt // 2
            _bitonic_sort(a, low, k, 1)
            _bitonic_sort(a, low + k, k, 0)
            _bitonic_merge(a, low, cnt, dire)

    _bitonic_sort(array, 0, len(array), 1)
    yield array, [-1]