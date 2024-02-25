import cms_open_data_tools as codt
import sys

#'TTTo2L2Nu'

if len(sys.argv)==1:
    codt.pretty_print(codt.datasets)
    exit()

dataset = sys.argv[1]

nevents = -1
if len(sys.argv)>2:
    nevents = int(sys.argv[2])

if nevents == -1:
    codt.generate_nicks_recipe(codt.datasets,dataset,IS_MC=True, number_of_events=-1, RUN=True)
    codt.generate_nicks_recipe(codt.datasets,dataset,IS_MC=True, number_of_events=100, RUN=True)
else:
    codt.generate_nicks_recipe(codt.datasets,dataset,IS_MC=True, number_of_events=nevents, RUN=True)

