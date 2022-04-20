#!/bin/bash


cd SHNtupliser/test

python submitJobFromFile.py --input Run3ExtendedEtaEle --pattern Electron --config ../../../SHarper/TrigNtup/test/egRegTreeMakerRefinedAOD.py --cmsswVersion 1223 --shNtupVersion EgRegTree --dryRun False 

cd -
