import pandas as pd

thermo = pd.read_csv(amplicons)

primer_pairs = amplicons[['Forward Primer Query Name', 'Reverse Primer Query Name']].to_dict('records')

# Checking if the primer pairs target the same virus based on the first element of the primer names
# Returns a tuple of primer pair names if both belong to the same virus

primer_check = []

for p in primer_pairs:
    if p.values()[0].split('_')[0] == p.values()[1].split('_')[0]:
        primer_check.append((p.values()[1], p.values()[0]))

# Check if the length of the list of primer pairs for the same virus is the same as the number of primer pairs being analyzed 

len(primer_check) == len(primer_pairs)

# Alternative pandas solution that returns a new column with the boolean test result of comparing the first
# element of the forward primer name vs. the first element of the reverse primer name

amplicons['Same Target'] = amplicons['Forward Primer Query Name'].str.split('_').apply(pd.Series,1)[0] == amplicons['Reverse Primer Query Name'].str.split('_').apply(pd.Series,1)[0]

# Check how many Trues we get

len(amplicons.loc[amplicons['Same Target'] == True])

# Alternatively

amplicons['Same Target'].value_counts()
