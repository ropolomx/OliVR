#!/usr/env/bin python3

from Bio import SeqIO
from Bio import Entrez
import collections

Entrez.email = "r.ortegapolo@uleth.ca"

accession = []

for rec in SeqIO.parse('atyp_pv.fna', 'fasta'):
    accession.append(rec.name.split("|")[3])

handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")

species = []

for rec in SeqIO.parse(handle, "gb"):
    species.append(rec.annotations['organism'])

speciesfreqs = collections.Counter(species)

speciesfreqsDict = dict(speciesfreqs)
