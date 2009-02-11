#ifndef SHARPER_HEEPANALYZER_HEEPCUTVALUES
#define SHARPER_HEEPANALYZER_HEEPCUTVALUES

//This is a simple struct to hold the values of a particular set of cuts, eg barrel heep cuts
//Some cuts dont make sense for both barrel and endcap but its easier to just have a common struct


#include <iostream>
#include <string>

namespace edm{
  class ParameterSet;
}
  
namespace heep {
  struct EleCutValues  {
  public:
    int cutMask;  
    int validEleTypes;
    double minEt;
    double minEta;
    double maxEta;
    double maxDEtaIn;
    double maxDPhiIn;
    double maxHadem;
    double maxSigmaIEtaIEta;
    double minE2x5Over5x5;
    double minE1x5Over5x5;
    double isolEmHadDepth1ConstTerm;
    double isolEmHadDepth1GradTerm;
    double isolEmHadDepth1GradStart;
    double isolHadDepth2ConstTerm;
    double isolHadDepth2GradTerm;
    double isolHadDepth2GradStart;
    double isolPtTrksConstTerm;
    double isolPtTrksGradTerm;
    double isolPtTrksGradStart;
    int isolNrTrksConstTerm;
    
    explicit EleCutValues(const edm::ParameterSet& iConfig);

  };
}


 


#endif
