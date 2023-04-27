# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial
import sys
import CRABClient
from CRABClient.UserUtilities import config

config = config()

submitVersion = "Egamma_regression_electron_realIC"

mainOutputDir = '/store/group/phys_egamma/ec/prrout/EGM_regression_Ntuples_04102022/%s' % submitVersion

config.General.transferLogs = False

config.JobType.pluginName  = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName  = '/afs/cern.ch/work/p/prrout/public/EGM_Reco_commissioning_work_Run3/Energy_Regression_Train_04102022/CMSSW_12_2_3/src/SHarper/TrigNtup/test/egRegTreeMakerRefinedAOD.py'

config.JobType.sendExternalFolder = True
config.JobType.allowUndistributedCMSSW = True

config.Data.allowNonValidInputDataset = True

config.Data.inputDBS = 'global'
config.Data.publication = False

#config.Data.publishDataName = 
config.Site.storageSite = 'T2_CH_CERN'
config.General.workArea = 'crab_%s' % submitVersion

##### now submit DATA
config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'Ntuple_V1')
config.Data.splitting     = 'FileBased' # on MC
#config.Data.splitting     = 'LumiBased' # on data 
#config.Data.splitting     = 'EventBased' # on PrivateMC
config.Data.totalUnits      = -1
#config.Data.lumiMask      = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt' #UL2018  
config.Data.unitsPerJob   = 40
#config.Data.unitsPerJob   = 200


config.General.requestName = 'job_DoubleElectron_FlatPt-1To500_13p6TeV'
config.Data.inputDataset   = '/DoubleElectron_FlatPt-1To500_13p6TeV/Run3Winter22DR-FlatPU0to70_122X_mcRun3_2021_realistic_v9-v2/AODSIM'

    
    

    
    
    

    
    






