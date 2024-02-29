import os
###############################################################################################
datasets = {}

datasets['collision'] = {}
datasets['MC'] = {}

datasets['collision']['Doublemuon'] = []
file = {"tag":'DoubleMuon_2015_0000', \
        "GCP_location":'/content/colab_directory/DoubleMuon_2015_0000_NANOAOD.root', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/Run2015D/DoubleMuon/MINIAOD/16Dec2015-v1/10000/00348932-30A8-E511-989A-00261894394A.root', \
        "OpenDataPortal_link": 'XXX'}
datasets['collision']['Doublemuon'].append(file)

datasets['MC']['TTbar'] = []
TTbar_file = {"tag":'TTbar_2015_0000', \
        "GCP_location":'/content/colab_directory/TTbar_2015_0000_NANOAOD.root', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/TTTo2L2Nu_13TeV_ScaleUp-powheg/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/00000/0413DE46-4CD1-E511-A9A5-00266CFFC43C.root', \
        "OpenDataPortal_link": 'XXX'}
datasets['MC']['TTbar'].append(TTbar_file)

################################################################################
# New for 2024!
dataset_name = 'TTTo2L2Nu_2015'
datasets['MC'][dataset_name] = []
# File
entry = {"tag":'0000', \
        "GCP_location":'/content/colab_directory/MC_TTTo2L2Nu_2015_nevents_100_0000_NanoAOD.root', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/TTTo2L2Nu_13TeV-powheg/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/00000/02A468DA-E8B9-E511-942C-0022195E688C.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/19958'}
datasets['MC'][dataset_name].append(entry)

# File
entry = {"tag":'0001', \
        "GCP_location":'/content/colab_directory', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/TTTo2L2Nu_13TeV-powheg/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/00000/02E52F5F-C5B9-E511-A146-001EC9ADE1C2.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/19958'}
datasets['MC'][dataset_name].append(entry)

# File
entry = {"tag":'0002', \
        "GCP_location":'/content/colab_directory', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/TTTo2L2Nu_13TeV-powheg/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/007FEAD7-53BA-E511-B4F0-001EC9ADE6D1.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/19958'}
datasets['MC'][dataset_name].append(entry)

# File
entry = {"tag":'0003', \
        "GCP_location":'/content/colab_directory', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/TTTo2L2Nu_13TeV-powheg/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/088F2069-56BA-E511-B4F9-0025900EB52A.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/19958'}
datasets['MC'][dataset_name].append(entry)

# File
entry = {"tag":'0004', \
        "GCP_location":'/content/colab_directory', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/TTTo2L2Nu_13TeV-powheg/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/163BBEE5-54BA-E511-A348-0022195D96C0.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/19958'}
datasets['MC'][dataset_name].append(entry)

################################################################################

dataset_name = 'TTToSemiLep_2015'
datasets['MC'][dataset_name] = []
# File
entry = {"tag":'0000', \
        "GCP_location":'', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/TTToSemiLeptonic_13TeV-powheg/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/00001/180C1AEA-20CA-E511-A65D-02163E01649D.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/19966'}
datasets['MC'][dataset_name].append(entry)

entry = {"tag":'0001', \
        "GCP_location":'', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/TTToSemiLeptonic_13TeV-powheg/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/00001/2AD47C2F-0BC7-E511-8B23-3417EBE74303.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/19966'}
datasets['MC'][dataset_name].append(entry)

entry = {"tag":'0002', \
        "GCP_location":'', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/TTToSemiLeptonic_13TeV-powheg/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/10001/265FA771-1EC5-E511-8463-0025907750A0.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/19966'}
datasets['MC'][dataset_name].append(entry)

entry = {"tag":'0003', \
        "GCP_location":'', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/TTToSemiLeptonic_13TeV-powheg/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/10001/D837FF2F-9AC6-E511-928C-001EC9B21C7C.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/19966'}
datasets['MC'][dataset_name].append(entry)

entry = {"tag":'0004', \
        "GCP_location":'', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/TTToSemiLeptonic_13TeV-powheg/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/20000/04C72F5E-ADC1-E511-ACD2-002590D0B00A.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/19966'}
datasets['MC'][dataset_name].append(entry)

###############################################################################

datasets['MC']['DY'] = []
dy_file = {"tag":'DY_2015_0000', \
        "GCP_location":'/content/colab_directory/DY_2015_0000_NANOAOD.root', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/10000/06761E14-6ED8-E511-BBCD-0025905B85B2.root', \
        "OpenDataPortal_link": 'XXX'}
datasets['MC']['DY'].append(dy_file)

datasets['collision']['TAU'] = []
TAU_file = {"tag":'tau_2015_0000', \
        "GCP_location":'/content/colab_directory/tau_2015_0000_NANOAOD.root', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/Run2015D/Tau/MINIAOD/16Dec2015-v1/00000/04F3F3CA-61B0-E511-9B3F-A0369F7FE970.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/24117'}
datasets['collision']['TAU'].append(TAU_file)

datasets['MC']['Darkmatter'] = []
darkmatter_file = {"tag":'darkmatter_2015_0000', \
        "GCP_location":'/content/colab_directory/darkmatter_2015_0000_NANOAOD.root', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/DarkMatter_MonoPhoton_AV_Mx-500_Mv-10000_gDMgQ1_LO_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/80000/AA064591-DBD8-E511-A193-0025904C66EE.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/16515'}
datasets['MC']['Darkmatter'].append(darkmatter_file)

###############################################################################################

###############################################################################################
def generate_nicks_recipe(all_datasets, dataset_name, IS_MC=False, number_of_events=-1, RUN=False):

    print(number_of_events)
    tag_nevents = 'default'
    if number_of_events == -1:
        tag_nevents = 'nevents_all'
    else:
        tag_nevents = f'nevents_{number_of_events}'
    
    '''
    for i in datasets['collision']:
      if datasets['collision'][i] == x:
        print(f'cmsDriver.py --python_filename {configuration_file} --eventcontent NANOAOD --datatier NANOAOD \
    --fileout file:{x[0]["tag"]}_{tag_nevents}_nanoaod.root --conditions 106X_dataRun2_v36 --step NANO \
    --filein file:{miniAOD}_miniaod.root --era Run2_25ns,run2_nanoAOD_106X2015 --no_exec --data -n {number_of_events} \
    --customise PhysicsTools/PFNano/pfnano_cff.PFnano_customizeData_onlyPF\n')
        print('collision')
    '''

    if IS_MC:
        datasets = all_datasets['MC'][dataset_name]
        print("Generating commands to run...")
        #counter = 0
        for dataset in datasets:
            print("##############\nData set....\n##############\n")
            print(dataset)
            #print()

            '''
            if counter<2:
                counter += 1
                continue
            '''

            #counter_tag = f"{counter:04d}"
            counter_tag = dataset['tag']

            miniAOD = dataset["miniAOD_file"]
            miniAOD_local_file = miniAOD.split('/')[-1]
            configuration_file = f'MC_{dataset_name}_{counter_tag}_{tag_nevents}_cfg.py'
            output_file = f'MC_{dataset_name}_{tag_nevents}_{counter_tag}_NanoAOD.root'

            print("# Run this command to copy over the file...\n")
            cmd = f'xrdcp {miniAOD} {miniAOD_local_file}\n'
            print(cmd)
            if RUN:
                os.system(cmd)
            print()

            print("# Then run this command to create the configuration file convert from miniAOD to NanoAOD...\n")
            cmd = f'cmsDriver.py --python_filename {configuration_file} --eventcontent NANOAODSIM --datatier NANOAODSIM '
            cmd += f' --fileout file:{output_file} --conditions 102X_mcRun2_asymptotic_v8 --step NANO '
            cmd += f' --filein file:{miniAOD_local_file} --era Run2_25ns,run2_nanoAOD_106X2015 --no_exec --mc -n {number_of_events} '
            cmd += f' --customise PhysicsTools/PFNano/pfnano_cff.PFnano_customizeMC_onlyPF'
            print(cmd)
            if RUN:
                os.system(cmd)
            print()
            print()

            print("# Then run this command to actually do the conversion from miniAOD to NanoAOD...it may take a while\n")
            cmd = f'time cmsRun {configuration_file}'
            print(cmd)
            if RUN:
                os.system(cmd)
            print()

            print("# The file that was produced should be the following. Upload this file to GCP")
            print("# and add the file name to the dictionary.\n")
            print(output_file)
            print()
            print()

            print("# Copying over the file to CERNBox space...")
            cmd = f"cp {output_file} /afs/cern.ch/user/m/mbellis/eos_storage/data_files/."
            print(cmd)
            if RUN:
                os.system(cmd)

            #counter += 1

###############################################################################################
'''

###############################################################################################

def gcp_location(d, x, y):
  for i in d[x][y]:
    gcp_location_list = []
    for j in i.keys():
      if j == 'GCP_location':
        for f in d[x][y]:
          gcp_location_list.append(f[j])
  return gcp_location_list

###############################################################################################
def pretty_print(datasets):
  for colMC in datasets.keys():
    print(f"{colMC} -------------")
    #print(colMC,datasets[colMC])
    names = datasets[colMC].keys()
    #output = f"{names}"
    #print(output)
    for name in names:
      output = f"\t{name}"
      print(output)
      sub_datasets = datasets[colMC][name]
      for sub_dataset in sub_datasets:
        #print(sub_dataset)
        for key in sub_dataset.keys():
          output = f"\t\t{key:20s}: {sub_dataset[key]}"
          print(output)
  print()

###############################################################################################

'''
