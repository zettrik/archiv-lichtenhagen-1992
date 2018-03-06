#!/bin/bash
fp="/home/zotero"

## rename image sources in zoteros csv exportfile
sed -i 's/\.tif/\.jpg/g' ${fp}/lichtenhagen.csv 
#exit 0

## convert imageformats
count=0
for fdir in `find ${fp}/storage -type d -print`; do
    echo ${fdir}
    for tif in `find ${fdir} -name '*.tif' -print`; do
        echo ${tif};
        filename=`basename ${tif} .tif`
        dirname=`dirname ${tif}`
        convert ${dirname}/${filename}.tif -quality 92 ${dirname}/${filename}.jpg
        echo "tiff nr.: $((++count))"
    done
done
echo "number of convertes tif images: ${count}"

