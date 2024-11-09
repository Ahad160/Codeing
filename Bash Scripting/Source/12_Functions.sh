#!/bin/bash


Funtion() {
    echo "Funtion is has been Called"
}

echo "Funtion is available"
Funtion

# Passing Argument
Funtion() {

    echo "Funtion No- $1 has been Called"
}


echo "Funtion (1-5) Available"
Funtion 5