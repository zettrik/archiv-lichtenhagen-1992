# Scripts and documentation for building an webarchive with 

## Documentation
* https://systemausfall.org/wikis/howto/DigitaleArchive -- development (in German) 

## Workflow
* collect content in Zotero
* export Zotero content in csv format
* convert tif files in jpg
* text recognition for all images
* generate index for content
* import index in Drupal


## Zotero export and conversation
* on Debian9 you'll need tesseract, imagemagick (convert), rsync, screen
* sync Zotero database
* export the library to /data/zotero/lichtenhagen.csv
```
cd /data/archiv-lichtenhagen-1992
git pull
cd helper-scripts
./file-count.sh
./file-convert.sh (takes approx. 1h)
./file-ocr.sh (can start while conversion is still running; takes approx. 12h)
rsync -avz --delete --delete-excluded --exclude='*.tif' --bwlimit=2M /data/zotero/ archive-server:/data/zotero-export/ (takes approx. 1h)
```

## Drupal 8 import and index creation

## Links 
### ocr and pdf/a
* https://github.com/Flameeyes/unpaper
* http://www.konradvoelkel.com/2013/03/scan-to-pdfa/
* https://williamjturkel.net/2013/07/06/doing-ocr-using-command-line-tools-in-linux/

### search engine
* https://www.lullabot.com/articles/indexing-content-from-drupal-8-to-elasticsearch
* optimize elasticsearch optimieren
 * kibana for data analysis
 * test opensearchserver http://wiki.univention.de/index.php?title=Cool_Solution_-_OpenSearchServer

