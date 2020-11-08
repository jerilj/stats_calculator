def is_valid(data):
    if len(data) == 0:
        raise Exception("Data is empty")
    valid = True
    for i in data:
        if type(i) == int or type(i) == float:
            valid = True
        else:
            valid = False
            break
    return valid
