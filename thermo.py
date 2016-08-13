from Bio import SeqIO
import csv
import pandas as pd

def thermo_info(fasta):
    for rec in SeqIO.parse(fasta, 'fasta'):
        seq = rec.seq
        conc = float(0.0000001)
        oligo_func = str.upper('primer')
        name = rec.name
        strand_type = str.upper('dna')
        
        yield (
        seq, 
        oligo_func, 
        strand_type,
        name
        )

def thermo_report(reportpath, result):
    headers = ['Sequence', 'Concentration', 'Strand Type', 'Function', 'Name']
    with open(reportpath, 'w') as f:
        out = csv.writer(f, delimiter = ',')
        out.writerow(headers)
        for t in thermo_table(result):
            out.writerow(t)

# Enter specific concentration
thermo_DF = pd.read_csv('bhc_thermoblast.csv')
thermo_DF.loc[thermo_DF.Name.str.contains('BVD|BoHV|RPV'), 'Concentration'] = 0.2
thermo_DF.loc[thermo_DF.Name.str.contains('VSV'), 'Concentration'] = 0.3
thermo_DF.loc[thermo_DF.Name.str.contains('PPV'), 'Concentration'] = 0.3
thermo_DF.loc[thermo_DF.Name.str.contains('BTV'), 'Concentration'] = 1.4
thermo_DF['Concentration'] = thermo_DF['Concentration'] * 0.000001
