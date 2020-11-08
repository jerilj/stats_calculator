def addition(a, b):
    return a + b


def add_list(data):
    total = 0
    for i in data:
        total = addition(total, i)
    return total
