#!/bin/bash


cd SHNtupliser/test

python submitJobFromFile.py --input Input_file_ele_ECALIdealIC_postEE_12_4_X --pattern Electron --config ../../../SHarper/TrigNtup/test/egRegTreeMakerRefinedAOD.py --cmsswVersion 1246 --shNtupVersion EgRegTree --dryRun False 

cd -
