#!/bin/bash

# Sent Standard Error To Null
find /etc -type f 1> /dev/null

# Sent Standard Output & Standard Error To Null
find /etc -type f &> /dev/null

# Senting Standard Output & Standard Error To Diffrent Paht
find /etc -type f 1> Output.txt 2> Error.txt