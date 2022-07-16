def create_query(cmd, value, file_list):
    if cmd == "filter":
        result = filter(lambda y: value.upper() in y, file_list)
        return result
    if cmd == "map":
        value = int(value)
        result = map(lambda x: x.split()[value], file_list)
        return result
    if cmd == "unique":
        return list(set(file_list))
    if cmd == "sort":
        reverse = "value" == "desc"
        res = sorted(file_list, reverse=reverse)
        return res
    if cmd == "limit":
        value = int(value)
        res = list(file_list)[:value]
        return res
