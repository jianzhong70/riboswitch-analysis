#!/bin/bash

for name in 3d2g 3d2v 3d2x apo
do
  cd $name
  for i in 1 2 3 4 
  do
    mkdir md$i
    cd md$i
    pmemd.cuda -O -i ../01-min.in -p ../comp_wat.prmtop -c ../comp_wat.inpcrd -o 01-min.out -x 01-min.nc -ref ../comp_wat.inpcrd -r 01-min.rst
    pmemd.cuda -O -i ../02-min.in -p ../comp_wat.prmtop -c 01-min.rst -o 02-min.out -x 02-min.nc -ref 01-min.rst -r 02-min.rst
    pmemd.cuda -O -i ../03-nvt.in -p ../comp_wat.prmtop -c 02-min.rst -o 03-nvt.out -x 03-nvt.nc -ref 02-min.rst -r 03-nvt.rst
    pmemd.cuda -O -i ../04-npt.in -p ../comp_wat.prmtop -c 03-nvt.rst -o 04-npt.out -x 04-npt.nc -ref 03-nvt.rst -r 04-npt.rst
    pmemd.cuda -O -i ../05-cmd.in -p ../comp_wat.prmtop -c 04-npt.rst -o 05-cmd.out -x 05-cmd.nc -r 05-cmd.rst
  cd ../
  done
cd ../
done
