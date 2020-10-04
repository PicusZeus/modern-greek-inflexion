from copy import deepcopy

def dict_of_dicts_merge(x, y):

    z = {}
    if isinstance(x, set):
        x.update(y)
        return x
    elif isinstance(x, str):
        return x + ',' + y
    overlapping_keys = x.keys() & y.keys()
    for key in overlapping_keys:
        z[key] = dict_of_dicts_merge(x[key], y[key])
    for key in x.keys() - overlapping_keys:
        z[key] = deepcopy(x[key])
    for key in y.keys() - overlapping_keys:
        z[key] = deepcopy(y[key])
    return z

def merging_all_dictionaries(*dics):
    if len(dics) > 2:
        first = dics[0]
        second = dics[1]
        rest = dics[2:]
        merged = dict_of_dicts_merge(first, second)
        merging_all_dictionaries(merged, *rest)
    elif len(dics) == 2:
        return dict_of_dicts_merge(*dics)
    else:
        return dics[0]
