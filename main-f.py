from src.formate import Formation
from geowords import terms_1014 as word


f = Formation(word)
f.markdown_table(["Terms", "Translation"])
# f.input_to_list()
