from devtool.timing import timer
from src.search import Engine
from data.datapath import paths

timer()
execution = Engine(path=paths("geology", "marinegeology",
                              "mineral", "highschoolearth",
                              "geography", "pedology", "astronomy"))
#from geowords import terms_1014 as terms
#sr = execution.multiple_search([i[0] for i in terms])
#compare(terms, sr)
execution.endless_mode()
