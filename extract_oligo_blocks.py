from Bio import AlignIO 
from Bio import SeqIO
from collections import defaultdict
import re
import numpy as np
import pandas as pd
import argparse

def arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument('--oligos', required=True, help='Fasta file with oligo sequences')
    parser.add_argument('msa', help="FASTA of multiple sequence alignment")

    return parser.parse_args()

def read_alignment(multifasta):
    aln = AlignIO.read(multifasta, 'fasta')
    return aln

def read_oligos(oligonucleotides):
    oligo_names = (rec.id for rec in SeqIO.parse(oligonucleotides, 'fasta'))
    return oligo_names

def get_blocks(alignment, molecules):
    
    block_dict = defaultdict(dict)
    
    for m in molecules:
        for a in alignment:
            if re.search(m, a.id):
                block_dict[a.id] = dict((int(index), value) 
                                        for index, value in enumerate(a.seq) if value != '-')
            
    block_slices = {k: [alignment[:, sorted(list(v))[0]:sorted(list(v))[-1]]]
                           for (k,v) in block_dict.items()}

    return block_slices

def sequence_arrays(block_segments):

    slice_arrays = defaultdict(list)

    for k,v in block_segments.items():
        for rec in v:
            slice_arrays[k] = np.array([list(rec)], np.character, order="F")

    return slice_arrays

def concat_dataframes(aln, array_blocks):
    
    sequence_dfs = {k: pd.DataFrame(v[0], index=[rec.id for rec in aln]) for k,v in array_blocks.items()}
    binary_dfs = {k: (sequence_dfs[k].ix[k] == sequence_dfs[k]).astype(int) for k in sequence_dfs}
    
    for b in binary_dfs.values():
            b['Mismatches'] = b.shape[1] - b.sum(axis=1)
            
    concatenations = {k:pd.concat([v,v2],1) for k,v in sequence_dfs.items() for k2,v2 in binary_dfs.items() if k == k2}
    
    return concatenations

def tabulations(concats):
    
    [v.to_csv(str(k)+'.csv') for k,v in concats.items()]

def main():

    args = arguments()
    alignment = read_alignment(args.msa)
    assay = read_oligos(args.oligos)
    blocks = get_blocks(alignment, assay)
    sequence_matrices = sequence_arrays(blocks)
    concatenated_dfs = concat_dataframes(alignment, sequence_matrices)
    tabulations(concatenated_dfs)

if __name__ == '__main__':
    main()
