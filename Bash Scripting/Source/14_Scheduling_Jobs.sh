#!/bin/bash

File=Run.log

echo "Program is Run at- $date" > $File

#Scheuling Job
# at 19:50 -f ./14.sh

#List Scheuling Job
# atq

# Remove a Scheuling Job
# atrm 3 //Job ID