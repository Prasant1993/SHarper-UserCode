#!/bin/bash

cd SHNtupliser/test

python submitJobFromFile.py --input ULSamples --pattern DoubleElectron --config ../../../SHarper/TrigNtup/test/egRegTreeMakerRefinedAOD.py --cmsswVersion 1061 --shNtupVersion EgRegTree --dryRun False 

cd -
