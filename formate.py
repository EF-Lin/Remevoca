from dataclasses import dataclass
import pyperclip
from geowords import terms_1014 as word


@dataclass
class Formation:
    data: list

    def markdown_table(self, first: list, copy=True):
        d2 = [first, ["-----" for _ in range(len(first))]]
        d2.extend(self.data)
        c1 = '|'
        s1 = ""
        for i in d2:
            s1 += c1
            for j in i:
                s1 += f"{str(j)} {c1}"
            s1 += '\n'
        print(s1)
        pyperclip.copy(s1) if copy else 0


if __name__ == "__main__":
    f = Formation(word)
    f.markdown_table(["Terms", "Translation"])
