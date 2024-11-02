#!/bin/bash

command=/usr/bin/htop

if [ -f $command ]
then
    echo "Software is Installed"
    $command
else
    echo "Software is Not Installed"
fi        