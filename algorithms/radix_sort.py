def sort(array: list[int]):
    """Radix Sort"""

    RADIX = 10
    #buckets = tuple([] for i in range(RADIX))
    buckets = [[] for i in range(RADIX)]  # 3% faster than a tuple in Python 3.7.4 32-bit on Windows 10 Home.

    # sort
    maxLength = False
    tmp = -1; placement = 1
    while not maxLength:
        maxLength = True
        
        # split input between lists
        for i in array:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)
            passed = False
            if maxLength and tmp > 0:
                passed = True
                maxLength = False
                yield array, [i]
            if not passed:
                yield array, [i]
        
        # empty lists into input array
        a = 0
        for bucket in buckets:
            for i in bucket:
                array[a] = i
                yield array, [i]  # Before the a += 1 because of IndexError
                a += 1
            bucket.clear()
        
        # move to next digit
        placement *= RADIX
        
        yield array, []
