#!/bin/bash

cd SHNtupliser/test

python submitJobFromFile.py --input Run3_120XNtup_Samples --pattern 1To500 --config ../../../SHarper/TrigNtup/test/egRegTreeMakerRefinedAOD.py --cmsswVersion 1200 --shNtupVersion EgRegTree --dryRun False 

cd -
