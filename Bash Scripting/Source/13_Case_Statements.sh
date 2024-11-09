#!/bin/bash

echo "Give This Script a Rateing*"

echo "1 - *"
echo "2 - **"
echo "3 - ***"
echo "4 - ****"
echo "5 - *****"

read user

case $user in
    1) echo "Script Rateing is *";;
    2) echo "Script Rateing is **";;
    3) echo "Script Rateing is ***";;
    4) echo "Script Rateing is ****";;
    5) echo "Script Rateing is *****";;
    *) echo "Enter valid Rateing"
esac    

