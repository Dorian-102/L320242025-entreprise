d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"c": 4,"e": 5, "f": 6}

def combinedict(dict1, dict2):
    dictemp= {}
    for d1key, d2val in zip(dict1.keys(), dict2.values()):
        dictemp[d1key] = d2val
    return dictemp

dict3 = combinedict(d1, d2)

print(f'dict1: {d1}')
print(f'dict2: {d2}')
print(f'dict3: {dict3}')
