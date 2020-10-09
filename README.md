Sam Harper's usercode area which has some useful tools for e/gamma. In general anything here super useful will migrate to other repos. 

Its mainly here as it was used to generate the ntuples for the regression so as per E/gamma policy it has to be in the E/gamma area.

## install instructions
In the current state, I recommend installing into CMSSW_10_6_1/src
Clone the branch called 'forIlya' as shown below
```
cd CMSSW_10_6_1/src
git clone -b forIlya git@github.com:wrtabb/SHarper-UserCode.git
```
First double check that you have write permissions since I had this problem
```
./checkwrite
```
Assuming your write permissions are fine, simply run:
```
./submit.sh
```
This should work out of the box with no modifications.
The root files will be output here:
```
/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/ikrav/1061/EgRegTree/AODSIM
```
