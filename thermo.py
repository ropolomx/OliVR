#!/usr/bin/env python3

from Bio import SeqIO
import csv
import pandas as pd
import argparse

def arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument('--thermo-table', default='./ThermoBLAST_table.csv',
                        help = 'CSV output file with table for ThermoBLAST submission')

    parser.add_argument('primers', help='MultiFASTA file with primer sequences to evaluate')

    return parser.parse_args()

def thermo_info(fasta):
    for rec in SeqIO.parse(fasta, 'fasta'):
        seq = rec.seq
        conc = float(0.0000001)
        oligo_func = str.upper('primer')
        strand_type = str.upper('dna')
        name = rec.name
        
        yield (
        seq,
        conc,
        strand_type,
        oligo_func, 
        name
        )

def thermo_report(fasta,reportpath):
    headers = [
            'Sequence',
            'Concentration',
            'Strand Type',
            'Function',
            'Name'
            ]

    with open(reportpath, 'w') as f:
        out = csv.writer(f, delimiter = ',')
        out.writerow(headers)
        for t in thermo_info(fasta):
            out.writerow(t)

def main():

    args = arguments()
    thermo_report(args.primers, args.thermo_table)

if __name__ == '__main__':
    main()

# Enter specific concentration
# thermoDF = pd.read_csv('bhc_thermoblast.csv')

# thermoDF.loc[thermoDF.Name.str.contains('BVD|BoHV|RPV'), 'Concentration'] = 0.2
# thermoDF.loc[thermoDF.Name.str.contains('VSV'), 'Concentration'] = 0.3
# thermoDF.loc[thermoDF.Name.str.contains('PPV'), 'Concentration'] = 0.3
# thermoDF.loc[thermoDF.Name.str.contains('BTV'), 'Concentration'] = 1.4

# thermoDF.loc[thermoDF.Name.str.contains('FMDV|KBH|Circo'), 'Concentration'] = 1.25
# thermoDF.loc[thermoDF.Name.str.contains('SVDV|VESV|ASFV|PRRSV'), 'Concentration'] = 0.625
# thermoDF['Concentration'] = thermoDF['SVDV|VESV|ASFV|PRRSV'] * 0.000001


# thermoDF['Concentration'] = thermoDF['Concentration'] * 0.000001
