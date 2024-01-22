from copy import deepcopy
from modern_greek_accentuation.resources import vowels


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


def update_forms_with_prefix(verb_temp, prefix: [str]):
    new_dict = {}
    for key, item in verb_temp.items():
        if isinstance(item, set):
            new_set = set()
            for form in item:
                if form[0] in vowels:
                    new_form = '/'.join([prefix[1] + f for f in form.split('/')])
                else:
                    new_form = '/'.join([prefix[0] + f for f in form.split('/')])
                new_set.add(new_form)

            new_dict[key] = new_set
        elif isinstance(item, dict):

            new_dict[key] = update_forms_with_prefix(item, prefix)
        elif isinstance(item, str):
            #'ων/ούσα/ον'
            new_dict[key] = '/'.join([prefix + f for f in item.split('/')])
        else:
            new_dict[key] = item
    return new_dict

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
