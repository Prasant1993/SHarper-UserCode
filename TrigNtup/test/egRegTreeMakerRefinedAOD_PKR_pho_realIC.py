#isCrabJob=False #script seds this if its a crab job

# Import configurations
import FWCore.ParameterSet.Config as cms
import os
import sys
# set up process
from Configuration.Eras.Era_Run3_cff import Run3
process = cms.Process("HEEP", Run3)

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('analysis') 
options.register('isMC',True,options.multiplicity.singleton,options.varType.bool," whether we are running on MC or not")
options.parseArguments()


#process = cms.Process("process", Run3)

#print(options.inputFiles)
#process.source = cms.Source("PoolSource",
#                            fileNames = cms.untracked.vstring(options.inputFiles),  
#                          )

process.source = cms.Source("PoolSource",
                                # replace 'myfile.root' with the source file you want to use                        
                                fileNames = cms.untracked.vstring(
            '/store/mc/Run3Summer22DR/DoublePhoton_FlatPT-5to500_13p6TeV/AODSIM/FlatPU0to70_124X_mcRun3_2022_realistic_v12-v2/2810000/0996a327-8643-44e7-9781-442e5d04646a.root'
            #'/store/mc/Run3Summer22DR/DoubleElectron_FlatPT-1to500_13p6TeV/AODSIM/FlatPU0to70_124X_mcRun3_2022_realistic_v12-v2/2820000/02afda55-bfb4-4cd3-a50c-b2e2365796a6.root',
            #'/store/mc/Run3Summer22DR/DoubleElectron_FlatPT-1to500_13p6TeV/AODSIM/FlatPU0to70_124X_mcRun3_2022_realistic_v12-v2/2820000/02d4e437-db22-4710-99ab-7fca92a0c3ed.root',
            #'/store/mc/Run3Summer22DR/DoubleElectron_FlatPT-1to500_13p6TeV/AODSIM/FlatPU0to70_124X_mcRun3_2022_realistic_v12-v2/2820000/042a5d73-f515-4ae5-98f5-691971197d68.root',
            #'/store/mc/Run3Summer22DR/DoubleElectron_FlatPT-1to500_13p6TeV/AODSIM/FlatPU0to70_124X_mcRun3_2022_realistic_v12-v2/2820000/04615d08-e70b-47f5-933f-5311026b0607.root'

))


# initialize MessageLogger and output report
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(5000),
    limit = cms.untracked.int32(10000000)
)

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )

#Load geometry
process.load("Configuration.Geometry.GeometryRecoDB_cff")
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.autoCond import autoCond
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '124X_mcRun3_2022_realistic_v12', '')
#if options.isMC: 
#    process.GlobalTag = GlobalTag(process.GlobalTag, '105X_mc2017_realistic_v5', '')
#    process.GlobalTag = GlobalTag(process.GlobalTag, '122X_mcRun3_2021_realistic_v9-v2', '')
#else:
#    from SHarper.SHNtupliser.globalTags_cfi import getGlobalTagNameData
#    globalTagName = getGlobalTagNameData(datasetVersion)
#    process.GlobalTag = GlobalTag(process.GlobalTag, globalTagName,'')
#    process.GlobalTag = GlobalTag(process.GlobalTag, '103X_dataRun2_v6_AC_v01', '')

process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Geometry.CaloEventSetup.CaloTowerConstituents_cfi")
process.load("Configuration.StandardSequences.Services_cff")

# set the number of events
#process.maxEvents = cms.untracked.PSet(
#    input = cms.untracked.int32(options.maxEvents)
#)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('egm_reg_DoublePho_realIC_Tree_24022023.root'))

process.egRegTreeMaker = cms.EDAnalyzer("EGRegTreeMaker",
                                        verticesTag = cms.InputTag("offlinePrimaryVertices"),
                                        rhoTag = cms.InputTag("fixedGridRhoFastjetAllTmp"),
                                        genPartsTag = cms.InputTag("genParticles"),
                                        puSumTag = cms.InputTag("addPileupInfo"),
                                     #   scTag = cms.VInputTag("particleFlowSuperClusterECAL:particleFlowSuperClusterECALBarrel","particleFlowSuperClusterECAL:particleFlowSuperClusterECALEndcapWithPreshower"),
                                        scTag = cms.VInputTag("particleFlowEGamma",),
                                        scAltTag = cms.VInputTag("particleFlowSuperClusterECALNoThres:particleFlowSuperClusterECALBarrel","particleFlowSuperClusterECALNoThres:particleFlowSuperClusterECALEndcapWithPreshower"),
                                        ecalHitsEBTag = cms.InputTag("reducedEcalRecHitsEB"),
                                        ecalHitsEETag = cms.InputTag("reducedEcalRecHitsEE"),
                                        elesTag = cms.InputTag("gedGsfElectrons"),
                                        phosTag = cms.InputTag("gedPhotons"),
                                        elesAltTag = cms.VInputTag(),
                                        phosAltTag = cms.VInputTag(),
                                        )

process.load("SHarper.TrigNtup.rePFSuperCluster_cff")


process.p = cms.Path(process.rePFSuperClusterThresSeq*process.egRegTreeMaker)

outputFile = cms.string('egm_reg_DoublePho_realIC_Tree_24022023.root')

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('AODSIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fileName = cms.untracked.string(options.outputFile.replace(".root","_EDM.root")),
    outputCommands = cms.untracked.vstring('drop *',
                                           "keep *_*_*_HEEP",
                                    )                                                                              )

#process.out = cms.EndPath(process.AODSIMoutput)


def setEventsToProcess(process,eventsToProcess):
    process.source.eventsToProcess = cms.untracked.VEventRange()
    for event in eventsToProcess:
        runnr = event.split(":")[0]
        eventnr = event.split(":")[2]
        process.source.eventsToProcess.append('{runnr}:{eventnr}-{runnr}:{eventnr}'.format(runnr=runnr,eventnr=eventnr))

#eventsToProcess = ['1:1:9322756']
#setEventsToProcess(process,eventsToProcess)

