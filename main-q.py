from dictionary.words import words as word
from src.question import Question_generator
from data.datapath import paths

qg = Question_generator(data=word, path=paths("geology", "marinegeology",
                                               "mineral", "highschoolearth",
                                               "geography", "pedology", "astronomy"))
qg.default_random_mode()
