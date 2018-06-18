#!/bin/bash

head -n1 lichtenhagen.csv > little.csv
cat lichtenhagen.csv | grep \"I- | wc -l
cat lichtenhagen.csv | grep \"I- >> little.csv
echo "#I - Vorgeschichte" > ../lh92-index/docs/vorgeschichte.md
./index-generator.py >> ../lh92-index/docs/vorgeschichte.md


head -n1 lichtenhagen.csv > little.csv
cat lichtenhagen.csv | grep \"II-A | wc -l
cat lichtenhagen.csv | grep \"II-A >> little.csv
echo "#II-A - Kommune Rostock" > ../lh92-index/docs/II-A.md
./index-generator.py >> ../lh92-index/docs/II-A.md

head -n1 lichtenhagen.csv > little.csv
cat lichtenhagen.csv | grep \"II-B | wc -l
cat lichtenhagen.csv | grep \"II-B >> little.csv
echo "#II-B - Land" > ../lh92-index/docs/II-B.md
./index-generator.py >> ../lh92-index/docs/II-B.md

head -n1 lichtenhagen.csv > little.csv
cat lichtenhagen.csv | grep \"II-C | wc -l
cat lichtenhagen.csv | grep \"II-C >> little.csv
echo "#II-C - Bund" > ../lh92-index/docs/II-C.md
./index-generator.py >> ../lh92-index/docs/II-C.md

head -n1 lichtenhagen.csv > little.csv
cat lichtenhagen.csv | grep \"II-D | wc -l
cat lichtenhagen.csv | grep \"II-D >> little.csv
echo "#II-D - International" > ../lh92-index/docs/II-D.md
./index-generator.py >> ../lh92-index/docs/II-D.md


head -n1 lichtenhagen.csv > little.csv
cat lichtenhagen.csv | grep \"III-A | wc -l
cat lichtenhagen.csv | grep \"III-A >> little.csv
echo "#III-A - Kommune Rostock" > ../lh92-index/docs/III-A.md
./index-generator.py >> ../lh92-index/docs/III-A.md

head -n1 lichtenhagen.csv > little.csv
cat lichtenhagen.csv | grep \"III-B | wc -l
cat lichtenhagen.csv | grep \"III-B >> little.csv
echo "#III-B - Land" > ../lh92-index/docs/III-B.md
./index-generator.py >> ../lh92-index/docs/III-B.md

head -n1 lichtenhagen.csv > little.csv
cat lichtenhagen.csv | grep \"III-C | wc -l
cat lichtenhagen.csv | grep \"III-C >> little.csv
echo "#III-C - Bund" > ../lh92-index/docs/III-C.md
./index-generator.py >> ../lh92-index/docs/III-C.md

head -n1 lichtenhagen.csv > little.csv
cat lichtenhagen.csv | grep \"III-D | wc -l
cat lichtenhagen.csv | grep \"III-D >> little.csv
echo "#III-D - International" > ../lh92-index/docs/III-D.md
./index-generator.py >> ../lh92-index/docs/III-D.md

