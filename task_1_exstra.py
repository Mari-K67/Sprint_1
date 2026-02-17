def delete_duplicates(tickets):
    unic_tikets = {}
    list_for_check = []
    for key,value in tickets.items():
        if value not in list_for_check:
            list_for_check.append(value)
            unic_tikets[key] = value
    return unic_tikets


def join_dictonaries(types, tickets):
    result = {}
    
    for key_types, value_types in types.items():
        result[value_types] = []

    for key_tikets, value_tikets in tickets.items():
        if key_tikets in types:
            value_types = types[key_tikets]
            result[value_types].append(value_tikets)

    return result