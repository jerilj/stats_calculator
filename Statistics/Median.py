def median(data):
    data.sort()
    size = len(data)
    if size % 2 == 0:
        middle_1 = int(size/2)
        middle_2 = int(middle_1-1)
        return (data[middle_1]+data[middle_2])/2
    else:
        middle = int((size-1)/2)
        return data[middle]

