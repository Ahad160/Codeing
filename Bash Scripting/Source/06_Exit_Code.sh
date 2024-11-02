#!/bin/bash

package=htop

sudo apt install htop 

if  [ $? = 0 ]
then
    echo "Package is Successfully Installed"
else
    echo "Package is Not Successfully Installed"
fi    