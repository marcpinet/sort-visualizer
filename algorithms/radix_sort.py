import time


def sort(array: list[int]):
    """Radix Sort"""
    start_time = time.time()

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
            if maxLength and tmp > 0:
                maxLength = False
                yield array, [i], time.time() - start_time
        
        # empty lists into input array
        a = 0
        for bucket in buckets:
            for i in bucket:
                array[a] = i
                yield array, [array[a], i], time.time() - start_time  # Before the a += 1 because of IndexError
                a += 1
            bucket.clear()
        
        # move to next digit
        placement *= RADIX
        
        yield array, [-1], time.time() - start_time
