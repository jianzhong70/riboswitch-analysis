#!/bin/bash
export CUDA_VISIBLE_DEVICES=0


for ((i = 1; i < 41; i = i+1))

do
  mkdir md$i
  cd md$i 
  pmemd.cuda -O -i ../md.in -p ../comp_wat.prmtop -c ../heat.rst -o md$i.out -r md$i.rst -x md$i.nc
#  pmemd.cuda -O -i ../gamd-restart.in -p ../comp_wat.prmtop -c md$i.rst -o gamd$i.out -x gmd$i.nc -r gamd$i.rst -gamd gamd$i.log
  cd ../
done
