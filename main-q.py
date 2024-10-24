from geowords import terms_1014 as words
from src.question import Question_generator
from datapath import paths

qq = Question_generator(data=words, path=paths("geology", "marinegeology",
                                               "mineral", "highschoolearth",
                                               "geography", "pedology", "astronomy"))
qq.default_random_mode()
