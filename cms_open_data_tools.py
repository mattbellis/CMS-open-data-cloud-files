###############################################################################################
datasets = {}

datasets['collision'] = {}
datasets['MC'] = {}

datasets['collision']['Doublemuon'] = []
file = {"tag":'Doublemuon_2015_0000', \
        "GCP_location":'/content/colab_directory/doublemuon_nanoaod.root', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/Run2015D/DoubleMuon/MINIAOD/16Dec2015-v1/10000/00348932-30A8-E511-989A-00261894394A.root doublemuon_miniaod.root', \
        "OpenDataPortal_link": 'XXX'}
datasets['collision']['Doublemuon'].append(file)

datasets['MC']['TTbar'] = []
TTbar_file = {"tag":'TTbar_2015_0000', \
        "GCP_location":'/content/colab_directory/TT_nanoaod.root', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/TTTo2L2Nu_13TeV_ScaleUp-powheg/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/00000/0413DE46-4CD1-E511-A9A5-00266CFFC43C.root', \
        "OpenDataPortal_link": 'XXX'}
datasets['MC']['TTbar'].append(TTbar_file)

datasets['MC']['DY'] = []
dy_file = {"tag":'DY_2015_0000', \
        "GCP_location":'/content/colab_directory/dy_nanoaod.root', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgrap    hMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/10000/06761E14-6ED8-E511-BBCD-0025905B85B2.root dy_miniaod.root', \
        "OpenDataPortal_link": 'XXX'}
datasets['MC']['DY'].append(dy_file)

datasets['collision']['TAU'] = []
TAU_file = {"tag":'tau_2015_0000', \
        "GCP_location":'/content/colab_directory/tau_nanoaod.root', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/Run2015D/Tau/MINIAOD/16Dec2015-v1/00000/04F3F3CA-61B0-E511-9B3F-A0369F7FE970.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/24117'}
datasets['collision']['TAU'].append(TAU_file)

datasets['MC']['Darkmatter'] = []
darkmatter_file = {"tag":'darkmatter_2015_0000', \
        "GCP_location":'/content/colab_directory/darkmatter_nanoaod.root', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/DarkMatter_MonoPhoton_AV_Mx-500_Mv-10000_gDMgQ1_LO_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/80000/AA064591-DBD8-E511-A193-0025904C66EE.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/16515'}
datasets['MC']['Darkmatter'].append(darkmatter_file)

###############################################################################################

###############################################################################################
def generate_nicks_recipe(x, number_of_events=-1):

  tag_nevents = 'default'
  if number_of_events == -1:
    tag_nevents = 'ALL_EVENTS_IN_MINIAOD'
  else:
    tag_nevents = f'nevents_{number_of_events}'

  miniAOD = f'DATA_miniAOD_{x[0]["tag"]}.root'
  configuration_file = f'{x[0]["tag"]}_cfg.py'
  print(f'xrdcp {x[0]["miniAOD_file"]} {miniAOD}\n')

  for i in datasets['collision']:
    if datasets['collision'][i] == x:
      print(f'cmsDriver.py --python_filename {configuration_file} --eventcontent NANOAOD --datatier NANOAOD \
  --fileout file:{x[0]["tag"]}_{tag_nevents}_nanoaod.root --conditions 106X_dataRun2_v36 --step NANO \
  --filein file:{miniAOD}_miniaod.root --era Run2_25ns,run2_nanoAOD_106X2015 --no_exec --data -n {number_of_events} \
  --customise PhysicsTools/PFNano/pfnano_cff.PFnano_customizeData_onlyPF\n')
      print('collision')

  for i in datasets['MC']:
    if datasets['MC'][i] == x:
      print(f'cmsDriver.py --python_filename {configuration_file} --eventcontent NANOAODSIM --datatier NANOAODSIM \
        --fileout file:{x[0]["tag"]}_{tag_nevents}_nanoaod.root --conditions 102X_mcRun2_asymptotic_v8 --step NANO \
        --filein file:{miniAOD} --era Run2_25ns,run2_nanoAOD_106X2015 --no_exec --mc -n {number_of_events} \
        --customise PhysicsTools/PFNano/pfnano_cff.PFnano_customizeMC_onlyPF\n')
      print('MC')

  print(f'cmsRun {configuration_file}')
