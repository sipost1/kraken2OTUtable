# kraken2OTU
Creates a simple OTU table from Kraken2 report. It extracts the OTU names and their read counts.

## Usage

### Preparations

First, you have to generate reports with kraken2 by using --report and --use-names options enabled. 

### Using the script

The script needs two arguments. First argument is the file, which will be used for the extraction. Second needs to be the desired level, like G, S, P, G1 etc...
You can use multiple levels, separated by commas.

Example:
```

python3 kraken2simplify.py AB1-191021.kraken2report G,P,S,G1,F

```

This command will create 5 different files, each containing the OTUs of given level. Example for genus:
From this (AB1-191021.kraken2report):
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
 ``` 
  to this (AB1-191021.kraken2report.G_only.tsv):

```
Pseudomonas     32447
Azotobacter     54
Permianibacter  13
Oblitimonas     11
Entomomonas     5
Acinetobacter   16974
Psychrobacter   79
Moraxella       70
Shewanella      24114
Parashewanella  14
```

