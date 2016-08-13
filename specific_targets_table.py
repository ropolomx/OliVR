from Bio import SeqIO
import argparse
import csv

def arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument('-o', '--table-name', default = 'target_specific_pairs.sts', help='Name of primer table output')
    
    parser.add_argument('primers', 
                        help='Fasta file with expanded degenerate primers')
    return parser.parse_args()

def cross_interactions(fasta):
    for rec in SeqIO.parse(fasta, 'fasta'):
        for rec2 in SeqIO.parse(fasta, 'fasta'):
            if (rec.name.split('_')[0], rec.name.split('_')[-2]) == \
                    (rec2.name.split('_')[0], rec.name.split('_')[-2]):
                
                forward = rec.seq
                reverse = rec2.seq
                primer_names = [rec.name, rec2.name]
                primer_pairs = '/'.join(primer_names)
                empty1 = ''
                empty2 = ''
                
                yield (
                    primer_pairs,
                    forward,
                    reverse,
                    empty1,
                    empty2
                    )

def tabular_sts(tablepath,fasta):
    
    with open(tablepath, 'w') as f:
    
        out = csv.writer(f, delimiter = '\t')
        
        for c in cross_interactions(fasta):
            out.writerow(c)

def main():

    args = arguments()

    cross_interactions(args.primers)

    tabular_sts(args.table_name, args.primers)

if __name__ == '__main__':
    main()
