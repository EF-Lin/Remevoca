from src.formate import Formation
from dictionary import words as word


f = Formation(word)
f.markdown_table(["Terms", "Translation"])
# f.input_to_list()
