def sort(array: list[int]):

    def merge_sort(start, end):

        if end - start > 1:
            middle = (start + end) // 2

            yield from merge_sort(start, middle)
            yield from merge_sort(middle, end)

            left = array[start:middle]
            right = array[middle:end]

            a = 0
            b = 0
            c = start
            
            # Visual only
            important_values = []
            important_values.extend(left)
            important_values.extend(right)

            while a < len(left) and b < len(right):
                if left[a] < right[b]:
                    array[c] = left[a]
                    a += 1
                else:
                    array[c] = right[b]
                    b += 1
                c += 1
                yield array, important_values

            while a < len(left):
                array[c] = left[a]
                a += 1
                c += 1
                yield array, important_values

            while b < len(right):
                array[c] = right[b]
                b += 1
                c += 1
                yield array, important_values

    yield from merge_sort(0, len(array))  # call inner function with start/end arguments
