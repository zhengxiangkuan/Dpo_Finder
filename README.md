# Dpo_Finder
A python script for the discovery of depolymerase sequences in phage genomes

# Introduction
This script is used to find depolymerase sequences in the phage genome. This script is based on blastp and is still very simple at the moment, but it's a work in progress!

# Required Packages
· ncbi-blast+

· biopython

# Input File
The -i parameter is entered as an amino acid sequence file in fasta format, ending in fa, faa and fasta.

# quick start
python Dpo_Finder.py -i example.faa -d sequences -o example.csv

# Usage
usage: Dpo_Finder.py [-h] -i INPUT -d DATABASE -o OUTPUT

Perform BLASTP search with custom database

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input query sequence file in FASTA format
  -d DATABASE, --database DATABASE
                        Name of the BLASTP database to be searched
  -o OUTPUT, --output OUTPUT
                        Output file for BLASTP best match results in TSV format
