#!/bin/bash

if [ $# -ne 1 ]
then
    echo "You did not give Argument"
    echo "Next Time, Try again with Arguments"
    exit 1
fi

echo "User Name is- $1"