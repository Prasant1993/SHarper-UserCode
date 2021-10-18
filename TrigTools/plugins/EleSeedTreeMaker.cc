#ifndef SHARPER_TRIGTOOLS_ECALRECHITCOLLCOMPARER
#define SHARPER_TRIGTOOLS_ECALRECHITCOLLCOMPARER

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/EgammaReco/interface/ElectronSeed.h"
#include "DataFormats/EgammaReco/interface/ElectronSeedFwd.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "SHarper/TrigTools/interface/TrigToolsStructs.h"

#include "TTree.h"

#include <vector>
#include <string>
#include <iostream>

namespace edm{
  class Event;
  class EventSetup;
  class ParameterSet;
}

class EleSeedTreeMaker : public edm::EDAnalyzer {
private:
  struct SeedInfo {
    float nrgy,eta,phi,pmDPhi1Pos,pmDPhi1Neg,pmDPhi2Pos,pmDPhi2Neg,pmDRZ1Pos,pmDRZ1Neg,pmDRZ2Pos,pmDRZ2Neg,hitsMask,subDet1,subDet2,ecalDriven,trackerDriven,nrHits;
    void fill(const reco::ElectronSeed& seed);
    static std::string contents(){return "nrgy/F:eta:phi:pmDPhi1Pos:pmDPhi1Neg:pmDPhi2Pos:pmDPhi2Neg:pmDRZ1Pos:pmDRZ1Neg:pmDRZ2Pos:pmDRZ2Neg:hitsMask:subDet1:subDet2:ecalDriven:trackerDriven:nrHits";}
    void clear(){nrgy=eta=phi=pmDPhi1Pos=pmDPhi1Neg=pmDPhi2Pos=pmDPhi2Neg=pmDRZ1Pos=pmDRZ1Neg=pmDRZ2Pos=pmDRZ2Neg=hitsMask=subDet1=subDet2=ecalDriven=trackerDriven=nrHits=-999;}
  };


  edm::EDGetTokenT<reco::ElectronSeedCollection> eleSeedsToken_;
  std::string treeName_;
  int datasetCode_;
  trigtools::EvtInfoStruct evtInfo_;
  SeedInfo seedInfo_;
  int seedNr_;
  int nrSeeds_;
  TTree* tree_; //we dont own this

 
public:
  explicit EleSeedTreeMaker(const edm::ParameterSet& iPara);
  ~EleSeedTreeMaker(){}
  void beginJob() override;
  void analyze(const edm::Event& iEvent,const edm::EventSetup& iSetup)override;
  //  virtual bool filter(edm::Event& iEvent,const edm::EventSetup& iSetup)override;


};

EleSeedTreeMaker::EleSeedTreeMaker(const edm::ParameterSet& iPara)
{
  eleSeedsToken_= consumes<reco::ElectronSeedCollection>(iPara.getParameter<edm::InputTag>("eleSeeds"));
  treeName_=iPara.getParameter<std::string>("treeName");
  datasetCode_=iPara.getParameter<int>("datasetCode");
}

void EleSeedTreeMaker::beginJob()
{
  edm::Service<TFileService> fs;
  fs->file().cd();
  tree_= new TTree(treeName_.c_str(),"tree");
  tree_->Branch("seed",&seedInfo_,seedInfo_.contents().c_str());
  tree_->Branch("evt",&evtInfo_,evtInfo_.contents().c_str());
  tree_->Branch("datasetCode",&datasetCode_,"datasetCode/I");
  tree_->Branch("seedNr",&seedNr_,"seedNr/I");
  tree_->Branch("nrSeeds",&nrSeeds_,"nrSeeds/I");
}

void EleSeedTreeMaker::analyze(const edm::Event& iEvent,const edm::EventSetup& iSetup)
{

  edm::Handle<reco::ElectronSeedCollection> eleSeedsHandle;  
  iEvent.getByToken(eleSeedsToken_,eleSeedsHandle);
  evtInfo_.fill(iEvent);
  nrSeeds_ = eleSeedsHandle->size();
  for(size_t seedNr = 0;seedNr<eleSeedsHandle->size();seedNr++){
    const auto& eleSeed = (*eleSeedsHandle)[seedNr];
    seedInfo_.fill(eleSeed);
    seedNr_ = seedNr;
    tree_->Fill(); 
  }
}
void EleSeedTreeMaker::SeedInfo::fill(const reco::ElectronSeed& seed)
{
  if(seed.caloCluster().isNonnull()){
    nrgy = seed.caloCluster()->energy();
    eta = seed.caloCluster()->eta();
    phi = seed.caloCluster()->phi();
  }else{
    nrgy=-1;eta=-1;phi=-1;
  }
  pmDPhi1Pos = seed.dPhiPos(0);
  pmDPhi1Neg = seed.dPhiNeg(0);
  pmDPhi2Pos = seed.dPhiPos(1);
  pmDPhi2Neg = seed.dPhiNeg(1);
  pmDRZ1Pos = seed.dRZPos(0);
  pmDRZ1Neg = seed.dRZNeg(0);
  pmDRZ2Pos = seed.dRZPos(1);
  pmDRZ2Neg = seed.dRZNeg(1);
  hitsMask = seed.hitsMask();
  subDet1 = seed.subDet(0);
  subDet2 = seed.subDet(1);
  ecalDriven = seed.isEcalDriven();
  trackerDriven = seed.isTrackerDriven();
  nrHits = seed.nHits();
}

DEFINE_FWK_MODULE(EleSeedTreeMaker);
#endif
