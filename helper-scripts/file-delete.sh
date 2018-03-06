#!/bin/bash
fp="/home/zotero"

counttif=0

for fdir in `find ${fp}/storage -type d -print`; do
    echo ${fdir}
    #for tif in `find ${fdir} -name '*.tif.jpg' -print`; do
    for tif in `find ${fdir} -name '*.tif' -print`; do
        echo ${tif}
        echo "tif nr.: $((++counttif))"
	#rm -i ${tif}
    done
done
echo "number of deleted tif images: ${counttif}"

