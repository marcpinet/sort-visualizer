def sort(array: list[int]):
    """Gravity/Bead Sort"""

    ref = [range(x) for x in array]  # for reference

    inter = []  # for intermediate
    ind = 0  # for index
    prev = sum([1 for x in ref if len(x) > ind])  # prev for previous
    while prev:
        inter.append(range(prev))
        ind += 1
        prev = sum([1 for x in ref if len(x) > ind])
        yield array, [ind - 1]

    ind = 0
    prev = sum([1 for x in inter if len(x) > ind])
    out = []

    while prev:
        out.append(prev)
        ind += 1
        prev = sum([1 for x in inter if len(x) > ind])
        tmp = [x for x in out]
        tmp.extend([x for x in array if x not in tmp])
        yield tmp[::-1], [prev]
        
    out = out[::-1]

    yield out, []
