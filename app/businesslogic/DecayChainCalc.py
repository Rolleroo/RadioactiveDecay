## Building the decay chain calculator

def hl_get(table, get_nuc):
    import csv

    lookup = open(table)

    for row in csv.reader(lookup):
        if get_nuc in row[0]:
            hl = row[1]
            print(hl)


hl_get("TrialLookup.csv", "A-90")

def daughter_get(table, get_nuc):
    import csv

    lookup = open(table)

    for row in csv.reader(lookup):
        if get_nuc in row[0]:
            daughter = row[3]
            print(daughter)

daughter_get("TrialLookup.csv", "A-90")