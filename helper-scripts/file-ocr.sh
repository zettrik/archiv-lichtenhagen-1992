#!/bin/bash
fp="/home/zotero"

## ocr 
count=0
for fdir in `find ${fp}/storage -type d -print`; do
    echo ${fdir}
    for tif in `find ${fdir} -name '*.jpg' -print`; do
        echo ${tif};
        filename=`basename ${tif} .jpg`
        dirname=`dirname ${tif}`
        tesseract ${dirname}/${filename}.jpg ${dirname}/${filename} -l deu -psm 1;
        echo "jpg nr.: $((++count))"
    done
done
echo "number of recognized jpg images: ${count}"
