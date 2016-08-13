import pandas as pd
from Bio import Entrez
from Bio import SeqIO
from collections import defaultdict

def read_data(epcr):
    # consider using the csv module to avoid loading into memory

    e_pcr = pd.read_table(epcr,
        names=[
            'Target',
            'Primer Pair', 
            'Strand', 
            'Hit Start', 
            'Hit End', 
            'Total Mismatches', 
            'Gaps', 
            'Size/Expected', 
            'Comments'
            ]
        )
    e_pcr = e_pcr.drop('Comments', 1)
    return read_data

def primer_pair_coverage(fasta, epcr):
    
    id_list = [rec.id for rec in SeqIO.parse('bluetongue_ViPR_nt.fasta', 'fasta')]
    
    e_pcr_targets = pd.Series(e_pcr.Target)
    
    # Dependent upon the format of the sequence headers
    e_pcr_targets = [t for t in e_pcr_targets.str.split('|').str[0].str.split(':').str[1]]

    set(e_pcr_targets).issubset(set(id_list))
    
    not_covered = [d for d in set(id_list).difference(set(e_pcr_targets))]

def extract_metadata(handle):

    source_serotype = defaultdict(dict)

    handle = Entrez.efetch(db="nuccore", id=id_list2, rettype="gb", retmode="text")

    for record in SeqIO.parse(handle, "gb"):
        source_serotype['Description'] = {record.id: record.description for (record.id, record.description) in record}

