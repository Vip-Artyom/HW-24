import re
from typing import Iterator, List, Any


def create_query(cmd: str, value: str, file_list: Iterator) -> List[Any]:
    if cmd == "filter":
        result = list(filter(lambda y: value.upper() in y, file_list))
        return result
    if cmd == "map":
        result = list(map(lambda x: x.split()[int(value)], file_list))
        return result
    if cmd == "unique":
        return list(set(file_list))
    if cmd == "sort":
        reverse = "value" == "desc"
        res = list(sorted(file_list, reverse=reverse))
        return res
    if cmd == "limit":
        res = list(file_list)[:int(value)]
        return res
    if cmd == "regex":
        regex = re.compile(value)
        res = list(filter(lambda x: regex.findall(x), file_list))
        return res
    return []
