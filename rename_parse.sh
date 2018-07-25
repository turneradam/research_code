#!/bin/bash

for file in *; 
do python3 ~/MEGA/research_code/scripts/fl_renamer.py "$file"; 
done

for file in *.txt;
do python3 ~/MEGA/research_code/scripts/fwhm.py "$file" "2";
done
