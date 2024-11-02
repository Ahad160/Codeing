#!/bin/bash

# Normal Way
expr 30 - 4

echo "30 - 4 = $(expr 30 - 4)"

# For Multiplication
expr 300 \* 5

# Using Variable

A=50
expr $A + 10