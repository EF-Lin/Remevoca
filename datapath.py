import os


data_path = r"./data/"
geology = r"國家教育研究院-地質學學術名詞.csv"
marinegeology = r"國家教育研究院-海洋地質學學術名詞.csv"
mineral = r"國家教育研究院-礦物學學術名詞.csv"
astronomy = r"國家教育研究院-天文學學術名詞.csv"
oceanology = r"國家教育研究院-海洋科學學術名詞.csv"
highschoolearth = "國家教育研究院-地球科學名詞-高中含以下地球科學學術名詞.csv"
geography = r"國家教育研究院-地理學名詞-高中含以下地理學學術名詞.csv"
pedology = r"國家教育研究院-土壤學學術名詞.csv"


def paths(*args) -> list:
    file_list = []
    for i in args:
        if i == "geology":
            file_list.append(geology)
        elif i == "marinegeology":
            file_list.append(marinegeology)
        elif i == "mineral":
            file_list.append(mineral)
        elif i == "astronomy":
            file_list.append(astronomy)
        elif i == "oceanology":
            file_list.append(oceanology)
        elif i == "highschoolearth":
            file_list.append(highschoolearth)
        elif i == "geography":
            file_list.append(geography)
        elif i == "pedology":
            file_list.append(pedology)
    return [os.path.normpath(f"{data_path}{i}") for i in file_list]
