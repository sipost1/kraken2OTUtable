# kraken2OTU

Creates a simple OTU table from Kraken2 reports. It extracts the OTU names and their read counts.

## Description

This script extracts read counts and OTU (species, genus or else) names from every kraken2 report file found in a given folder, and summarizes it in one OTU table (rows are OTUs, columns are samples).

## Usage

```
usage: kraken2otu.py [-h] --inputfolder INPUTFOLDER --level LEVEL [--extension EXTENSION]

optional arguments:
  -h, --help            show this help message and exit
  --inputfolder INPUTFOLDER, -i INPUTFOLDER
                        Input folder where report files can be found.
  --level LEVEL, -l LEVEL
                        Taxonomic level to extract from kraken2 report.
  --extension EXTENSION, -e EXTENSION
                        Extension of kraken2 report files. Default: .k2report
```


## Preparations

First, you have to generate reports with kraken2 by using --report and --use-names options enabled, then put the reports into one folder if they are not already there together. 

## Using the script

The script needs two arguments. One argument is the directory, where kraken2 reports can be found. The other needs to be the desired level, like G, S, P, G1 etc...
Output file will be placed into the input directory.
Sample names will be the filenames without extension.

Example:

```
python3 ./kraken2otu.py --inputfolder ./ --level g
```

This command will create one file, containing the OTUs of given level.
Example for genus:
From this (EB1-211103.k2report):

```
 72.33  440048  440048  U       0       unclassified
 27.67  168354  0       R       1       root
 27.67  168354  0       R1      131567    cellular organisms
 27.67  168354  1454    D       2           Bacteria
 23.46  142758  1804    P       1224          Proteobacteria
 17.38  105738  1070    C       1236            Gammaproteobacteria
  8.18  49747   24      O       72274             Pseudomonadales
  5.35  32566   36      F       135621              Pseudomonadaceae
  5.33  32447   4268    G       286                   Pseudomonas
  2.01  12219   3539    G1      196821                  unclassified Pseudomonas
  ...
```

  to this:
  (otu_table_G.tsv)

```
OTU    EB1-211103     EB2-211103
Pseudomonas     32447   67432
Azotobacter     54      5324
Permianibacter  13      621
Oblitimonas     11      534
Entomomonas     5       52
Acinetobacter   16974   16974
Psychrobacter   79      96
Moraxella       70      70
Shewanella      24114   24114
```

### Notes

The data here are from one file, I changed some values in EB1-* to get EB2 just to show how it works. It works fast with many files too. Probably it works with Kraken 1 too, but I did not have the oppurtunity to try it.
