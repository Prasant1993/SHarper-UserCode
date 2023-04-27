#!/bin/bash


cd SHNtupliser/test

python submitJobFromFile.py --input Input_file_ele_ECALIdealIC-v3 --pattern Electron --config ../../../SHarper/TrigNtup/test/egRegTreeMakerRefinedAOD.py --cmsswVersion 1223 --shNtupVersion EgRegTree --dryRun False 

cd -
