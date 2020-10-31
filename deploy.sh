#!/usr/bin/env bash

ERRORSTRING="eg: deploy live go"
if [ $# -eq 0 ]
    then
        echo $ERRORSTRING;
elif [ $1 == "live" ]
    then
        if [[ -z $2 ]]
            then
                echo "Running dry-run"
                rsync --dry-run -azz --force --delete --progress --exclude-from=rsync_exclude.txt -e "ssh -p22" ./ virtch.io:/srv/http/virtch
        elif [ $2 == "go" ]
            then
                echo "Running actual deploy"
                rsync -azz --force --delete --progress --exclude-from=rsync_exclude.txt -e "ssh -p22" ./ virtch.io:/srv/http/virtch
        else
            echo $ERRORSTRING;
        fi
fi

