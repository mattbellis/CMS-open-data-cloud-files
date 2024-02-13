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

codt.generate_nicks_recipe(codt.datasets,dataset,IS_MC=True, number_of_events=nevents)

