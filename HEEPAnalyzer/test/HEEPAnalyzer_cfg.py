#shamelessly stolen from PatAnalyzerSkeleton_cfg.py

# Import configurations
import FWCore.ParameterSet.Config as cms

# set up process
process = cms.Process("HEEP")

# initialize MessageLogger and output report
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkSummary = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(500),
    limit = cms.untracked.int32(10000000)
)
process.MessageLogger.cerr.FwkReport = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(500),
    limit = cms.untracked.int32(10000000)
)


process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )

# Load geometry
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('MC_31X_V3::All')
process.load("Configuration.StandardSequences.MagneticField_cff")


# this defines the input files
process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring('dummy'))
process.PoolSource.fileNames = [
    '/store/relval/CMSSW_3_2_6/RelValZEE/GEN-SIM-RECO/STARTUP31X_V7-v1/0013/9AB61A32-BA9A-DE11-8298-001D09F29619.root',
    '/store/relval/CMSSW_3_2_6/RelValZEE/GEN-SIM-RECO/STARTUP31X_V7-v1/0013/80CF3175-C59A-DE11-AB6E-0016177CA778.root',
    '/store/relval/CMSSW_3_2_6/RelValZEE/GEN-SIM-RECO/STARTUP31X_V7-v1/0013/7047D992-FC9A-DE11-863B-0019B9F72BAA.root',
    '/store/relval/CMSSW_3_2_6/RelValZEE/GEN-SIM-RECO/STARTUP31X_V7-v1/0013/5CC96C97-B59A-DE11-8CAA-0019B9F6C674.root',
    '/store/relval/CMSSW_3_2_6/RelValZEE/GEN-SIM-RECO/STARTUP31X_V7-v1/0013/126AA31F-BE9A-DE11-97E9-001D09F290BF.root']
#process.PoolSource.fileNames = ['file:/media/usbdisk1/zee_relVal_312_F0303A91-9278-DE11-AADC-001D09F25456.root']

# set the number of events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

#no configuration is necessary for us at the moment
process.load("PhysicsTools.PatAlgos.patSequences_cff");
# input heep analyzer sequence
process.load("SHarper.HEEPAnalyzer.HEEPAnalyzer_cfi")

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('heepEventOutput.root')
)


process.p = cms.Path(process.patDefaultSequence* #runs PAT 
                     process.heepAnalyzer) #runs heep analyzer


