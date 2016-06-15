#!/usr/bin/env python3

######################################################
## OliVR: Oligonucleotide Verification for Research ##
######################################################

from Bio import SeqIO
from multiprocessing import cpu_count
from io import StringIO
import rpy2.robjects as robjects
import subprocess
import sys
import os
import argparse

def arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('primers',
                        help = 'FASTA file with degenerate primers')
    
    return parser.parse_args()

def dscp_expand(primers_fasta):
    
    # assay = assay_name(primers_fasta)

    dscp = 'dscp.pl'
    return subprocess.call(dscp, input = primers_fasta) 

# def expand_grid(expanded):

def main():

    args = arguments()

    expand_degs = dscp_expand(args.primers)

if __name__ == '__main__':
    main()
