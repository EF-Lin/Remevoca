from geowords import terms_1014 as words
import random
import rich
from dataclasses import dataclass
from search import Engine
from datapath import paths


@dataclass
class Question_generator:
    data: list

    def __post_init__(self):
        self.len = len(self.data)
        self.engine = Engine(paths("geology","marinegeology",
                                   "mineral", "highschoolearth",
                                   "geography", "pedology"))

    def check_input(self, inp: str, num: int) -> bool:
        if inp.lower() == "eof":
            exit()
        elif inp.lower()[0:6] == "//test":
            try:
                num = eval(inp.split(' ')[1])
            except:
                num = 20
            self.test_mode(num)
            return False
        elif inp.lower()[0:2] == "//":
            self.engine.api_single_mode(inp[2:])
            return False
        elif inp.lower() == self.data[num][1].lower():
            rich.print("[b green]Correct" + '\n')
            return True
        else:
            rich.print(f"[red]Wrong, the answer is [green]{self.data[num][1]}\n")
            return False

    def single_question(self, index: int) -> bool:
        rich.print(f"[deep_sky_blue1]{self.data[index][0]}")
        ans = str(input("請輸入答案:"))
        return self.check_input(ans, index)

    def default_random_mode(self, old=-1):
        i = random.randint(0, self.len - 1)
        while i == old:
            i = random.randint(0, self.len - 1)
        f = self.single_question(i)
        while not f:
            f = self.single_question(i)
        self.default_random_mode(old=i)

    def test_mode(self, num: int):
        t = 0
        for i in range(num):
            t += 1 if self.single_question(random.randint(0, self.len - 1)) else 0
        rich.print(f"[green]{t}/{num}" if t/num >= 0.6 else f"[red]{t}/{num}\n")


if __name__ == "__main__":
    qq = Question_generator(words)
    qq.default_random_mode()
