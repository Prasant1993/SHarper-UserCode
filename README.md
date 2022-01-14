Sam Harper's usercode area which has some useful tools for e/gamma. In general anything here super useful will migrate to other repos. 

Its mainly here as it was used to generate the ntuples for the regression so as per E/gamma policy it has to be in the E/gamma area.

## install instructions
it needs to cloned into the directory SHarper in the $CMSSW_BASE/src directory. 

So when reading from Sam's version

```
cd $CMSSW_BASE/src
git clone git@github.com:Sam-Harper/usercode.git SHarper
```

or from the cms-egamma repo

```
cd $CMSSW_BASE/src
git clone git@github.com:cms-egamma/SHarper-UserCode.git SHarper
```

## instructions to produce ntuples

Create a file in the directory SHNtupliser/test/
Put the name of each sample you want to produce in this file. It must by the AOD version. For example:
```
/DoubleElectron_FlatPt-4000To5000/Run3Summer21DR-FlatPU0to70_120X_mcRun3_2021_realistic_v6-v1/AODSIM & -1 & -1 & 1.0 & 1.0 & 101 & 500 &
```
I don't recall the meanings of the options in the Input_File, but these are the options I always use. I'll have to track these down later
In the following code, I'll call this file 'Input_File'

```
python SHNtupliser/test/submitJobFromFile.py --input Input_File --pattern Electrons --config SHarper/TrigNtup/test/egRegTreeMakerRefinedAOD.py --cmsswVersion 1200 --shNtupVersion EgRegTree --dryRun False 
```
--input: The file which lists the samples to ntuplize
--pattern: A pattern to select which samples to ntuplize within the file
--config: This is the configuration file
--cmsswVersion: CMSSW version
--shNtupVersion: Ntuple version (not sure what other versions one could use; I've always just left this alone)
--dryRun: Can submit Crab job as a dry run if one chooses
