import os
###############################################################################################
datasets = {}

datasets['collision'] = {}
datasets['MC'] = {}

################################################################################
# New for 2024!
dataset_name = 'SingleMuon_2015D'
datasets['collision'][dataset_name] = []
# File
entry = {"tag":'0000', \
        "GCP_location":'/content/colab_directory/', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/Run2015D/SingleMuon/MINIAOD/16Dec2015-v1/10000/00006301-CAA8-E511-AD39-549F35AD8BC9.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/24119'}
datasets['collision'][dataset_name].append(entry)
# File
entry = {"tag":'0001', \
        "GCP_location":'/content/colab_directory/', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/Run2015D/SingleMuon/MINIAOD/16Dec2015-v1/10000/0034202D-A3A8-E511-BA9C-00259073E3DA.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/24119'}
datasets['collision'][dataset_name].append(entry)
# File
entry = {"tag":'0002', \
        "GCP_location":'/content/colab_directory/', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/Run2015D/SingleMuon/MINIAOD/16Dec2015-v1/10000/0043758E-ECA8-E511-B849-002618FDA287.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/24119'}
datasets['collision'][dataset_name].append(entry)
# File
entry = {"tag":'0003', \
        "GCP_location":'/content/colab_directory/', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/Run2015D/SingleMuon/MINIAOD/16Dec2015-v1/10000/004C08BC-C8A8-E511-943C-00266CFAE6E0.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/24119'}
datasets['collision'][dataset_name].append(entry)
# File
entry = {"tag":'0004', \
        "GCP_location":'/content/colab_directory/', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/Run2015D/SingleMuon/MINIAOD/16Dec2015-v1/10000/005416D9-E0A8-E511-8AA1-0CC47A4C8E46.root', \
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/24119'}
datasets['collision'][dataset_name].append(entry)

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

################################################################################

dataset_name = 'DYToLL_M_1_2015'
datasets['MC'][dataset_name] = []
# File
entry = {"tag":'0000', \
        "GCP_location":'', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/1AED42CB-51BB-E511-AADA-00259048AE52.root',
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/16490'}
datasets['MC'][dataset_name].append(entry)

entry = {"tag":'0001', \
        "GCP_location":'', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/34B7FBE5-80BB-E511-901F-001517E7410C.root',
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/16490'}
datasets['MC'][dataset_name].append(entry)

entry = {"tag":'0002', \
        "GCP_location":'', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/3C480167-61BB-E511-80D4-003048CB8610.root',
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/16490'}
datasets['MC'][dataset_name].append(entry)

entry = {"tag":'0003', \
        "GCP_location":'', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/4CFD0E08-66BB-E511-A67A-00304867FD83.root',
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/16490'}
datasets['MC'][dataset_name].append(entry)

entry = {"tag":'0004', \
        "GCP_location":'', \
        "miniAOD_file": 'root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/6A1EE854-4CBB-E511-837B-002590D9D990.root',
        "OpenDataPortal_link": 'https://opendata.cern.ch/record/16490'}
datasets['MC'][dataset_name].append(entry)


###############################################################################

###############################################################################################

###############################################################################################
def generate_nicks_recipe(all_datasets, dataset_name, IS_MC=False, number_of_events=-1, RUN=False):

    print(number_of_events)
    tag_nevents = 'default'
    if number_of_events == -1:
        tag_nevents = 'nevents_all'
    else:
        tag_nevents = f'nevents_{number_of_events}'
    
    EVENTCONTENT = "NANOAOD"
    CONDITIONS = "106X_dataRun2_v36"
    DATA_MC_FLAG = "--data"
    CUSTOMIZE = "PhysicsTools/PFNano/pfnano_cff.PFnano_customizeData_onlyPF"
    DATASETS = all_datasets['collision'][dataset_name]
    if IS_MC:
        EVENTCONTENT = "NANOAODSIM"
        CONDITIONS = "102X_mcRun2_asymptotic_v8"
        DATA_MC_FLAG = "--mc"
        CUSTOMIZE = "PhysicsTools/PFNano/pfnano_cff.PFnano_customizeMC_onlyPF"
        DATASETS = all_datasets['MC'][dataset_name]

    #if IS_MC:
    #datasets = all_datasets['MC'][dataset_name]
    print("Generating commands to run...")
    
    for dataset in DATASETS:
        print("##############\nData set....\n##############\n")
        print(dataset)
        
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

        '''
        for i in datasets['collision']:
          if datasets['collision'][i] == x:
            print(f'cmsDriver.py --python_filename {configuration_file} --eventcontent NANOAOD --datatier NANOAOD \
        --fileout file:{x[0]["tag"]}_{tag_nevents}_nanoaod.root --conditions 106X_dataRun2_v36 --step NANO \
        --filein file:{miniAOD}_miniaod.root --era Run2_25ns,run2_nanoAOD_106X2015 --no_exec --data -n {number_of_events} \
        --customise PhysicsTools/PFNano/pfnano_cff.PFnano_customizeData_onlyPF\n')
            print('collision')
        '''

        print("# Then run this command to create the configuration file convert from miniAOD to NanoAOD...\n")
        #cmd = f'cmsDriver.py --python_filename {configuration_file} --eventcontent NANOAODSIM --datatier NANOAODSIM '
        #cmd += f' --fileout file:{output_file} --conditions 102X_mcRun2_asymptotic_v8 --step NANO '
        #cmd += f' --filein file:{miniAOD_local_file} --era Run2_25ns,run2_nanoAOD_106X2015 --no_exec --mc -n {number_of_events} '
        #cmd += f' --customise PhysicsTools/PFNano/pfnano_cff.PFnano_customizeMC_onlyPF'
        cmd = f'cmsDriver.py --python_filename {configuration_file} --eventcontent {EVENTCONTENT} --datatier {EVENTCONTENT} '
        cmd += f' --fileout file:{output_file} --conditions {CONDITIONS} --step NANO '
        cmd += f' --filein file:{miniAOD_local_file} --era Run2_25ns,run2_nanoAOD_106X2015 --no_exec {DATA_MC_FLAG} -n {number_of_events} '
        cmd += f' --customise {CUSTOMIZE}'
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


###############################################################################################

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

