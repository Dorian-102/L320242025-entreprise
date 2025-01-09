def trouve_min_max(tup):
    if not tup:
        return None, None
    return min(tup), max(tup)

print(trouve_min_max((1, 2, 3, 4, 5)))

print(trouve_min_max((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

