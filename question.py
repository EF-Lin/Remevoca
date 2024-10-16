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

    def check_input(self) -> bool:
        if self.ans.lower() == "eof":
            exit()
        elif self.ans.lower()[0:6] == "//test":
            try:
                num = eval(self.ans.split(' ')[1])
            except:
                num = 20
            self.test_mode(num)
            return False
        elif self.ans.lower()[0:2] == "//":
            self.engine.api_single_mode(self.ans[2:])
            return False
        elif self.ans.lower() == self.data[self.i][not self.j].lower():
            rich.print("[b green]Correct\n")
            return True
        else:
            rich.print(f"[red]Wrong, the answer is [green]{self.data[self.i][not self.j]}\n")
            return False

    def single_question(self) -> bool:
        rich.print(f"[deep_sky_blue1]{self.data[self.i][self.j]}")
        self.ans = str(input("請輸入答案:"))
        return self.check_input()

    def default_random_mode(self, old=-1, super=True):
        self.i = random.randint(0, self.len - 1)
        self.j = random.choice([True, False]) if super else False
        while self.i == old:
            i = random.randint(0, self.len - 1)
        f = self.single_question()
        while not f:
            f = self.single_question()
        self.default_random_mode(old=self.i)

    def test_mode(self, num: int):
        t = 0
        old = self.i
        for i in range(num):
            self.i = random.randint(0, self.len - 1)
            t += 1 if self.single_question() else 0
        rich.print(f"[green]{t}/{num}" if t/num >= 0.6 else f"[red]{t}/{num}\n")
        self.i = old


if __name__ == "__main__":
    qq = Question_generator(words)
    qq.default_random_mode()
