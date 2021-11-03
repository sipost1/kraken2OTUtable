#!/usr/bin/python3


#Converts Kraken2 report to a simple OTU table.
#First argument must be the Kraken2 report file, while
#second argument should be the desired level (like species or genus, or multiple).

#If you want more levels at once,
#you can do it by specifying the levels
#delimited by commas.

#EXAMPLE:

#python3 kraken2otu.py AB1-190124_kraken2.report S,S1,G,P

from sys import argv
import os.path as PATH

def extract(file, lvl):

    directory = PATH.dirname(PATH.abspath(file))
    levels = lvl.split(",")
    for level in levels:
        dest_name = directory + "/" + PATH.basename(file) + "." + level + "_only.tsv"
        with open(file, "r") as ori, open(dest_name, "w") as dest:
            while(True):
                try:
                    line = ori.readline()
                    line = line.split("\t")
                    if line[3].strip(" ") == level:
                        dest.write("%s\t%s\n" % (line[5].strip(" ")[:-1], line[1]))

                except:
                    break
"""
        if argv[3] == "-f":
            from otuFilter import otu_filter
            otu_filter(dest_name, argv[4])
"""

if __name__ == "__main__":
    extract(argv[1], argv[2])
