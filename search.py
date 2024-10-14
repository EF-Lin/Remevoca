import csv
import rich
import os
from dataclasses import dataclass
from timing import timer
from datapath import paths


@dataclass
class Engine:
    path: list

    def __post_init__(self):
        self.data = []
        for i in self.path:
            self.data.extend(self.__load_data(i))

    @staticmethod
    def __load_data(path: str) -> list:
        return sorted(list(csv.reader(open(os.path.normpath(path), encoding="utf-8"))))

    def process_data(self):
        for i in range(len(self.data)):
            self.data[i][0] = self.data[i][0].lower()

    def __single_search(self, target: str) -> list:
        target = target.lower()
        for i in self.data:
            if target == i[0].lower() or target == i[1].lower():
                return i
        raise ValueError

    def __iterable_search(self, target: str) -> list:
        target = target.lower()
        result = []
        for i in self.data:
            if target == i[0].lower() or target == i[1].lower():
                result.append(i)
        if result != []:
            return result
        else:
            raise ValueError

    def multiple_search(self, target: list) -> list:
        result = [[i, ""] for i in target]
        for i in self.data:
            for j in range(len(target)):
                if target[j].lower() == i[0].lower():
                    result[j][1] = i[1]
                elif target[j].lower() == i[1].lower():
                    result[j][1] = i[0]
        return result

    def endless_mode(self):
        target = str(input())
        if target == "eof":
            exit()
        else:
            try:
                result = self.__iterable_search(target)
                for i in result:
                    rich.print(f"[b green]{i[0]}, {i[1]}")
            except Exception as ex:
                rich.print(f"[red]Error: {ex}")
            self.endless_mode()

    def api_single_mode(self, target):
        if target == "eof":
            exit()
        else:
            try:
                result = self.__iterable_search(target)
                for i in result:
                    rich.print(f"[b green]{i[0]}, {i[1]}")
            except Exception as ex:
                rich.print(f"[red]Error: {ex}")


def compare(a: list, b: list):
    for i, j, k in zip(a, b, range(len(a))):
        print(f"{k}: {i}/{j}") if i[1].lower() != j[1].lower() else 0


if __name__ == "__main__":
    timer()
    execution = Engine(path=paths("geology", "marinegeology",
                                  "mineral", "highschoolearth",
                                  "geography", "pedology"))
    #from geowords import terms_1014 as terms
    #sr = execution.multiple_search([i[0] for i in terms])
    #compare(terms, sr)
    execution.endless_mode()
