def mode(data):
    elm_count = {}
    count = 0
    elm = None
    for i in data:
        if i in elm_count:
            elm_count[i] = elm_count[i] + 1
        else:
            elm_count[i] = 1

    for i in elm_count:
        if elm_count[i] > count:
            most = i
            count = elm_count[i]

    return most
