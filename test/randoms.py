import random


def rand_int(a, b):
    return random.randint(a, b)


def rand_dec(a, b):
    return random.uniform(a, b)


def seed_int(a, b):
    random.seed(5)
    return random.randint(a, b)


def seed_dec(a, b):
    random.seed(5)
    return random.uniform(a, b)


def seed_list_int(a, b, n):
    random.seed(5)
    return random.choices(range(a, b), k=n)


def seed_list_dec(a, b, n):
    tmp = []
    counter = 0
    random.seed(5)
    while counter < n:
        val = random.uniform(a, b)
        tmp.append(val)
        counter = counter + 1
    return tmp


def select_item(data):
    return random.choice(data)


def seed_select_item(data):
    random.seed(5)
    return random.choice(data)


def select_items(data, n):
    return random.choices(data, k=n)


def seed_select_items(data, n):
    random.seed(5)
    return random.choices(data, k=n)
