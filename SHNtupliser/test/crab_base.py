from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'TOSED:REQUESTNAME'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True


config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'shNtupliser_autoGen_cfg.py'
config.JobType.maxJobRuntimeMin = 480
#config.JobType.maxMemoryMB = 3000
#config.JobType.numCores = 4
#config.JobType.inputFiles=['ged_regression_20161208.db',]
#TOSED:EXTRAJOBTYPEINFO

config.section_("Data")
config.Data.inputDataset = 'TOSED:DATASETPATH'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 'TOSED:UNITSPERJOB'
config.Data.totalUnits = 'TOSED:TOTALUNITS'
config.Data.publication = False
config.Data.publishDBS = 'phys03' 
config.Data.outputDatasetTag = 'TOSED:PUBLISHDATANAME'
config.Data.outLFNDirBase = 'TOSED:OUTPUTDIR'
config.Data.allowNonValidInputDataset = True
config.section_("Site")
config.Site.storageSite = "T2_CH_CERN"
config.Site.ignoreGlobalBlacklist = True
config.Site.whitelist = ['T2_FR_GRIF','T2_CH_CERN','T1_US_FNAL','T2_CH_CSCS','T1_FR_CCIN2P3','T2_ES_CIEMAT','T2_IN_TIFR','T1_DE_KIT','T1_IT_CNAF','T2_CN_Beijing','T2_US_UCSD','T2_UK_London_IC','T2_TW_NCHC','T2_DE_DESY','T1_UK_RAL','T2_ES_IFCA']
config.section_("User")
