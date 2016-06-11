#!/usr/bin/env python3

######################################################
## OliVR: Oligonucleotide Verification for Research ##
######################################################

from Bio import SeqIO
from multiprocessing import import cpu_count
from io import StringIO
import rpy2.robjects as robjects
import subprocess
import os
import argparse

def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('primers', help = 'FASTA file with degenerate primers'
            return parser.parse_args()

r.source("script.R")
