# Dpo_Finder
A python script for the discovery of depolymerase sequences in phage genomes

# Introduction
This script is used to find depolymerase sequences in the phage genome. This script is based on blastp and is still very simple at the moment, but it's a work in progress!

# Required Packages
· ncbi-blast+

· biopython

# Input File
The -i parameter is entered as an amino acid sequence file in fasta format, ending in fa, faa and fasta.

# Database building
        makeblastdb -in sequences -dbtype prot -out sequences

# quick start
## Single file
        python Dpo_Finder.py -i example.faa -d sequences -o example.csv
## Multiple files
        ls *.fa | while read id ; do python Dpo_Finder.py -i $id -d sequences -o $id.csv ; done

# Usage
    usage: python Dpo_Finder.py [-h] -i INPUT -d DATABASE -o OUTPUT
        
        Perform BLASTP search with custom database
        
        optional arguments:
        
          -h, --help            show this help message and exit
          
          -i INPUT, --input INPUT
                                Input query sequence file in FASTA format
                                
          -d DATABASE, --database DATABASE
                                Name of the BLASTP database to be searched
                                
          -o OUTPUT, --output OUTPUT
                                Output file for BLASTP best match results in TSV format
                        
# Output example
<img width="539" alt="output" src="https://user-images.githubusercontent.com/77312378/236362974-f8de7415-5c37-4697-bcf1-d3277a78960c.png">
