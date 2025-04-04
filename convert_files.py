import cms_open_data_tools as codt
import sys

#'TTTo2L2Nu_2015'
#'TTToSemiLep_2015'
RUN = True
#RUN = False

IS_MC=False
#IS_MC=True

if len(sys.argv)==1:
    codt.pretty_print(codt.datasets)
    exit()

dataset = sys.argv[1]

nevents = -1
if len(sys.argv)>2:
    nevents = int(sys.argv[2])

if nevents == -1:
    codt.generate_nicks_recipe(codt.datasets,dataset,IS_MC=IS_MC, number_of_events=-1, RUN=RUN)
    codt.generate_nicks_recipe(codt.datasets,dataset,IS_MC=IS_MC, number_of_events=100, RUN=RUN)
else:
    codt.generate_nicks_recipe(codt.datasets,dataset,IS_MC=IS_MC, number_of_events=nevents, RUN=RUN)

