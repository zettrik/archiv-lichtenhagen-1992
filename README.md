# Scripts and documentation for building an webarchive with mkdocs

## Installation & Setup
* grep zotero.csv
* apt install mkdocs
* mkdocs new lh92-index
* vi lh92-index/mkdocs.yml
* vi lh92-index/docs/index.md
* python script generates sites with markdown syntax
    * convert tif files in jpg
    * text recognition for all images
* mkdocs serve #for tesing purpose
* mkdocs build
* copy static html files to webserver


----
# Scripts and documentation for building an webarchive with Zotero and Zot_Bib_Web

## Documentation
* http://zot-bib-web.readthedocs.io/en/latest/#

## Installation
```
apt install python3-venv
python3 -m venv lh-py3env
git clone https://github.com/davidswelt/zot_bib_web.git
cd zot_bib_web
cp settings_example.py settings.py ## adapt to your needs
source lh-py3nv/bin/activate
pip3 install pyzotero

```

## Workflow
* collect content in Zotero
* generate index for content:
```
source lh-py3nv/bin/activate
cd zot_bib_web
./zot.py
```
* take a look at the generated html file


----
# Scripts and documentation for building an webarchive with Zotero and Drupal

## Documentation
* https://systemausfall.org/wikis/howto/DigitaleArchive -- development notes (in German) 

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

## Drupal 8
### Installation
* https://www.drupal.org/docs/develop/using-composer/using-composer-to-manage-drupal-site-dependencies
* https://www.lullabot.com/articles/drupal-8-composer-best-practices
```
aptitude install php7.0 php7.0-fpm php7.0-gd php7.0-mysql php7.0-mbstring phpunit
su webuser
wget https://getcomposer.org/installer
php installer
php composer.phar
composer create-project drupal-composer/drupal-project:8.x-dev archiv.lichtenhagen-1992.de --stability dev 

composer require drupal/ctools
composer update drupal/core --with-dependencies
```
* create database & set password for db user
* configure DNS an point your browser to new domain
* fill out forms

### Fine tuning
* for composer to work fine set higher php memory_limit
* install drush:
```
composer require drush/drush
../vendor/bin/drush
```
* install theme: https://www.drupal.org/project/magazine_lite

### Import and index creation
* create new content type
* add fields
* create taxonomie

* install restui: composer require drupal/restui
* activate rest + restui modules

* import content via script
* https://www.drupal.org/docs/8/core/modules/rest/3-post-for-creating-content-entities
* https://github.com/flesheater/python_drupal8_rest/blob/master/drupal8.py
* import csv with python to elasticsearch: https://elasticsearch-py.readthedocs.io/en/master/

## Elasticsearch samples
curl -X PUT 'localhost:9200/foo/bar/2' -d '{ "titel": "hahu", "autor": "bla" }'
curl -X GET 'localhost:9200/_search' -d '{ "query": { "match_all": {} }}'
curl -X GET 'localhost:9200/_aliases?pretty=1'
curl -X GET 'localhost:9200/_stats?pretty=1'

### Test elasticsearch
* restlet REST client: https://restlet.com/modules/client/?utm_source=DHC
* web front-end: https://github.com/mobz/elasticsearch-head

----
# Links 
## ocr and pdf/a
* https://github.com/Flameeyes/unpaper
* http://www.konradvoelkel.com/2013/03/scan-to-pdfa/
* https://williamjturkel.net/2013/07/06/doing-ocr-using-command-line-tools-in-linux/

## search engine
* https://www.lullabot.com/articles/indexing-content-from-drupal-8-to-elasticsearch
* http://wiki.univention.de/index.php?title=Cool_Solution_-_OpenSearchServer
* kibana for data analysis

