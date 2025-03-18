import os


data_path = r"./data/"
data = r"data.csv"


def paths(*args) -> list:
    file_list = []
    for i in args:
        if i == "data":
            file_list.append(data)
    return [os.path.normpath(f"{data_path}{i}") for i in file_list]
