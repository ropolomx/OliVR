import sys
from Bio import Entrez

def get_tax_id(species):

    """to get data from ncbi taxomomy, we need to have the taxid.  we can
    get that by passing the species name to esearch, which will return
    the tax id"""
    try:
        search_species = species.strip().replace(" ", "+")
        search = Entrez.esearch(term = search_species, db = "taxonomy", retmode = "xml")
        record = Entrez.read(search)
        return record['IdList'][0]
    except:
        print "\"{}\" gives a problem. Is the spelling correct?".format(species)
        print "Quitting to prevent any downstream problems..."
        sys.exit(2)

def get_tax_data(taxid):
    """once we have the taxid, we can fetch the record"""
    search = Entrez.efetch(id = taxid, db = "taxonomy", retmode = "xml")
    return Entrez.read(search)

def filter_tax_data(td, *tax):
    
    """Filters taxonomy data for
    the fields passed in by *tax"""
 
    out = []
    for item in td:
        
        current = item[0]
        lineage = { d['Rank'] : d['ScientificName'] for d in current['LineageEx']
                   if d['Rank'] in tax }
        out.append(lineage)
        
    return out

def get_hosts(filename):
    
    """Gets a list of hostnames from a comma
    or newline delimited file."""
    
    hosts = []
    with open(filename, 'r') as f:
        for line in f:
            if line != "\n": # ignores any spurious empty lines
                l = line.strip().split(',')
                hosts.extend(l)
    return hosts

def retrieve_taxonomy(email, hostfile, *tax):
    
    """Master function to run and
    pass arguments to the other functions"""
    
    Entrez.email = email
    hosts = get_hosts(hostfile)
    
    taxids = [get_tax_id(h) for h in hosts]

    taxdata_list = [get_tax_data(t) for t in taxids]

    taxonomy = filter_tax_data(taxdata_list, *tax)
    
    return taxonomy
