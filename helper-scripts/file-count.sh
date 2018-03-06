#!/bin/bash
fp="/home/zotero"

count_tif=0
count_jpg=0

for fdir in `find ${fp}/storage -type d -print`; do
    echo ${fdir}
    #for tif in `find ${fdir} -name '*.tif.jpg' -print`; do
    for tif in `find ${fdir} -name '*.tif' -print`; do
        echo ${tif};
        echo "tif nr.: $((++count_tif))"
    done
    for tif in `find ${fdir} -name '*.jpg' -print`; do
        echo ${tif};
        echo "jpg nr.: $((++count_jpg))"
    done
done
echo "number tif images: ${count_tif}"
echo "number jpg images: ${count_jpg}"

