from copy import deepcopy


def dict_of_dicts_merge(x, y):
    z = {}
    if isinstance(x, set):
        if isinstance(y, set):
            x.update(y)
            return x
        elif isinstance(y, str):
            y = set(y.split(','))
            x.update(y)
        return x
    elif isinstance(x, str):
        x = set(x.split(','))
        if isinstance(y, str):
            y = set(y.split(','))
        x.update(y)
        return x
    overlapping_keys = x.keys() & y.keys()
    for key in overlapping_keys:
        z[key] = dict_of_dicts_merge(x[key], y[key])
    for key in x.keys() - overlapping_keys:
        z[key] = deepcopy(x[key])
    for key in y.keys() - overlapping_keys:
        z[key] = deepcopy(y[key])
    if not z:
        raise ValueError
    return z


def merging_all_dictionaries(*dics):
    if len(dics) > 2:
        first = dics[0]
        second = dics[1]
        rest = dics[2:]
        merged = dict_of_dicts_merge(first, second)
        return merging_all_dictionaries(merged, *rest)

    else:
        if len(dics) == 2:

            merged = dict_of_dicts_merge(*dics)
            result = dict_of_dicts_merge(merged, merged)
            if not result:
                raise ValueError

            # merging_all_dictionaries(res)
        else:

            result = merging_all_dictionaries(dics[0], dics[0])
            if not result:
                raise ValueError

        return result
