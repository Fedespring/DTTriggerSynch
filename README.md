# DTTriggerSynch

How to use the cosmic analysis programs
==============
STEP 1: Histograms

     root DTNTuple_runXXXX.root
     root [0]DTTree->Process("histograms_HH_and_HL.C") 
     
This creates a root file (e.g. runXXXX_histograms.root) .

STEP 2: HL/HH

Compile histodiv.C , then use the output of step1:

      ./histodiv.exe 1 1 runXXXX_histograms.root
      
In the first argument 1 means 1 input file, for the second argument 1 means printgifs=true.

This creates hist_div_runXXXX.root , a txt file with the fit values and the gifs (optional).

How to use the collision analysis program
==============
Obtain t0s with:

     root DTNTuple_runXXXX.root
     root [0]DTTree->Process("t0_fitter.C") 
This creates the txt file with the t0s (fit_t0_runXXXX.txt). Make sure to cut out the first two lines of this txt before you use it for the corrections!

How to use the corrections program
==============
To calculate the corrections, first compile corrections_calculator.C , then:

      ./corrections_calculator.exe hist_div_runXXXX.root fit_t0_runXXXX.txt
      
About the cosmics calibration
===============
The python file RunTree_cosmics_Reco_as_ppcollisions_cfg_new.py is used to produce the ntuples for the cosmics analysis. It is necessary to reconstruct the cosmics as pp collisions to get the worst phase values of HH/HL.
You can change the file names, looking for them in DAS (cmsweb). Then, to run interactively simply do:

       cmsRun RunTree_cosmics_Reco_as_ppcollisions_cfg_new.py 

This will produce the DTNtuple.root in your directory. You can also send the jobs to crab the usual way:
https://twiki.cern.ch/twiki/bin/viewauth/CMS/DTAnalysisLHCRuns
     
      
      
      
      
