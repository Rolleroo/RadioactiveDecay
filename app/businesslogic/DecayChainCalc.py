## Building the decay chain calculator

## Creates the daughters list
daughters1 = []
daughters2 = []

i = 0
j = 0
k = 0
l = 0

## Function for looking up a radionuclide
def chain_get(table, get_nuc):  # defines the function and variables
    import csv  # imports the csv reader module

    lookup = open(table)   # defines the lookup table as the parameter input in "table"


## this small section determines if the nuclide in get nuc has $, denoting stable radionuclide, if so it breaks
    if '$' in get_nuc:
        print('End')
        sys.exit(1)
    else:
        print('Continue')

## This code searches for the nuclide input by the user and appends the daughter product to the daughters list

    for row in csv.reader(lookup):
        if get_nuc in row[0]:
            daughter1 = row[3]
            daughters1.append(daughter1)
            daughter2 = row[4]
            if daughter2 == '':
                print("I did nothing")
            else:
                daughters2.append(daughter2)
            print(daughters1)
            print(daughters2)
            print(daughter1)
            print(daughter2)



## Calling the commands to look up each daughter, I think these need to be in daughter order
chain_get("TrialLookup.csv", "A-90")
chain_get("TrialLookup.csv", daughters1[0])
chain_get("TrialLookup.csv", daughters1[1])

