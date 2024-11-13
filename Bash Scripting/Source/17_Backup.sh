#!/bin/bash

if [ $# -ne 2 ]
then
    echo "Backup <Source_Directory> <Target_Directory>"
    echo "Try Again"
    exit 1
fi

if ! command -v rsync > /dev/null 2>&1
then
    echo "rsync not install, INSTALL rsync and try again!"
    exit 2
fi

CurrentDate=$(date +%Y-%m-%d)

Rsync_Option="-avb --backup-dir $2/CurrentDate --delete --dry-run"

$(which rsync) $Rsync_Option $1 $2/current >> Backup_$CurrentDate.log
