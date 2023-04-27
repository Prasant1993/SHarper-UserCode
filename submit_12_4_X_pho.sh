#!/bin/bash


cd SHNtupliser/test

python submitJobFromFile.py --input Input_file_photon_ECALrealIC_postEE_12_4_X --pattern Photon --config ../../../SHarper/TrigNtup/test/egRegTreeMakerRefinedAOD.py --cmsswVersion 1246 --shNtupVersion EgRegTree --dryRun False 

cd -
