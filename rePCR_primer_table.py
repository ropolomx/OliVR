from Bio import SeqIO
import argparse
import csv

def arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument('-o', '--table-name', default = 'primers.prim', help='Name of primer table output')
    
    parser.add_argument('primers', 
                        help='Fasta file with expanded degenerate primers')
    return parser.parse_args()

def primer_info(fasta):
    for rec in SeqIO.parse(fasta, 'fasta'):
        primer_id = rec.name
        primer_seq = rec.seq
        
        yield (
            primer_id,
            primer_seq
            )

def primer_table(tablepath,fasta):
    with open(tablepath, 'w') as f:
    
        out = csv.writer(f, delimiter = '\t')
        
        for p in primer_info(fasta):
            out.writerow(p)

def main():
    
    args = arguments()
    primer_info(args.primers)
    primer_table(args.table_name, args.primers)

if __name__ == '__main__':
    main()
