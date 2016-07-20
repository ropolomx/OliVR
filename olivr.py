#!/usr/bin/env python3

######################################################
## OliVR: Oligonucleotide Verification for Research ##
######################################################

from Bio import SeqIO
from multiprocessing import cpu_count
from io import StringIO
import subprocess
import sys
import os
import argparse

def arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument('primers',
                        help = 'FASTA file with degenerate primers')
    parser.add_argument('mismatches',
                        help = 'Number of mismatches tolerated for the oligo search')
    return parser.parse_args()

# Goal: expand degenerate primers with the DSCP Perl script
# Only necessary if we are using e-PCR or PrimerBLAST

def dscp_expand(primers_fasta):
    
    # In this case, dscp.pl has been made executable with chmod + x in my system

    dscp = 'dscp.pl'
    
    run_dscp = subprocess.Popen(dscp, stdin=subprocess.PIPE, universal_newlines=True)
    
    return run_dscp.communicate(primers_fasta)

# Goal: generate table with all possible pairwise combinations of expanded forward and reverse primers 
# This table is the input for the standalone e-PCR software

# Ponder how to take advantage of e-PCR: (1) as a way to check how many amplicons we will get, 
# or (2) as a way to check the sensitivity of each primer individually. 

def run_e_PCR(forward, reverse, sequence_db):
    e_PCR = (
            'e-PCR', 
            '-w', '4', 
            '-n', mismatches, 
            '-o', , 
            '-t', '4', '../primers/pesti_primers_DF.sts',
            sequence_db
            )

    run_e_PCR = subprocess.call(e_PCR, universal_newlines=True)

def main():

    args = arguments()

    expanded_degeneracies = dscp_expand(args.primers)

if __name__ == '__main__':
    main()
