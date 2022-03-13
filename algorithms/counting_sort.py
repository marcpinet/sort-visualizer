def sort(array, digit=-1):
    """Counting Sort"""
    # Initialize the counting array
    counting_array = [0] * (max(array) + 1)

    # Count the number of occurrences of each element
    for element in array:
        counting_array[element] += 1

    # Compute the cumulative sum
    for i in range(1, len(counting_array)):
        counting_array[i] += counting_array[i - 1]

    # Create the output array
    output_array = [0] * len(array)

    # Copy the elements from the input array to the output array
    for i in range(len(array)):
        output_array[counting_array[array[i]] - 1] = array[i]
        counting_array[array[i]] -= 1
        yield array, [array[i]]

    # Copy the elements from the output array to the input array
    for i in range(len(array)):
        array[i] = output_array[i]
        yield array, [i]

    yield array, []
