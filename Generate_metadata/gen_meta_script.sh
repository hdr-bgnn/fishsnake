#!/bin/sh
# Usage : ./ download_script.sh Data/sub_list.csv
#path="$1/*.csv"

python ./gen_metadata.py $1
mv metadata.json Data/metadata.json
