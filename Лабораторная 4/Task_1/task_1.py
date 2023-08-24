import json

filename = 'input.json'
with open(filename, 'r') as file:
    data = json.load(file)


# TODO решите задачу
def task(data) -> float:
    list_ = [dict_["score"] * dict_["weight"] for dict_ in data]
    return sum(list_)


print("{:.3f}".format(task(data)))