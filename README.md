# riboswitch-analysis

These scripts, programes and data were used to probe conformational transition and recognition mechanism of eukaryotic riboswitches powered by thiamine pyrophosphate analogues.
1. The files apoforcein, d2xforcein, pyiforcein and tppforcein includes the files of paramters and coordinates for RNA force fields OL3, JIbb, ROC, Shaw and YIL together with infiles of MD simulations, which are applied to test the perforemance of RNA force fields.
2. The files apomd40, d2xmd40, pyimd40 and tppmd40  contains all parameters and input files used to perform multiple short molecular dynamics simulations.
3. The scripts forcetest.sh and run1.sh were employed to respectively run MD simulations for testing the RNA force fields and multiple short molecular dynamics simulations.
4. The scripts trajcombine.in and traj.in were utilized to separately combine multiple short trajectoies into a single trajectory for faciliating post-process analysis and tranform the nc format of trajectories into the xtc format.
5. The program msm3.ipunb was adopted to construct the Markov model for probing conformation transitions.
6. The scripts cpptraj.in and analysis.in were used to perform post-process analysis and principal component analysis by "cpptraj -i *.in".
7. The python program draw_arrows.py and extract_pc_test4.py were utilized to realize visualization of the results of principal component analysis.
8. The script timecorr.in was employed to perform time-correlation analysis of hydrogen bonds.
9. The other python programs were applied to realize visualization of data.
