# csel_openphilology_corpus

CSEL orpus based on https://github.com/OpenGreekAndLatin/csel-dev/ made available by http://www.dh.uni-leipzig.de/wo/

Text have been converted using https://github.com/cltk/capitains_corpora_converter

## How to update :

### With Capitains CLTK Converter from commandline

```shell
capitains-cltk-converter cloningdirectory --output path/to/this/repo/+/json --git https://github.com/OpenGreekAndLatin/csel-dev.git --credit "Open Philology, Humboldt Chair of Digital Humanities ( https://github.com/OpenGreekAndLatin/csel-dev )" --exclude-nodes tei:note tei:orig
```

### With this repo `update.py` file

Be sure to use Python3

```shell
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python update.py
rm -rf cloning
```