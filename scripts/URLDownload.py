## This python script downloads a txt file with the nuclear data and strips it down to useful CSV files

from urllib.request import urlretrieve as retrieve

url = 'http://amdc.in2p3.fr/nubase/nubase2016.txt'

# Specifies the loction of the data. Can't download directly from IAEA website gives 403 error. A mirror is used instead.

retrieve(url, 'Nudat.txt') # Retrieves the web location and saves in the route directory

##Needs an error handling facility so that the url can be manually entered if needed or a local file selected.

import re

## Strip out first line (neutron) which messes up the column formatting
## Not very elegant, sure I can combine with the functions to strip and clean the data.

with open('Nudat.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('Nudat2.txt', 'w') as fout:
    fout.writelines(data[1:])

## Cleans up the data to remove all unwanted columns
## Writes a file NudatClean.txt where with the cleaned up tables.

fin = open("Nudat2.txt", "rt")
fout = open("NudatClean.txt", "wt")

for line in fin:
        if len(line) > 106:
            fout.write(line[:18] + line[61:80] + line[109:] )

fin.close()
fout.close()

## Adds in the header rows

with open('NudatClean.txt', 'r') as original:
    data = original.read()
with open('NudatCleanHead.txt', 'w') as modified:
    modified.write("Am  P      Name   Life     Un Err     Decay\n" + data)

## Remove stable isotopes.

Stable = ['p-unst', 'stbl']

with open('NudatCleanHead.txt') as oldfile, open('NudatStrip2.txt', 'w') as newfile:
    for line in oldfile:
       if not any(Stable in line for Stable in Stable):
           newfile.write(line)

## This strips out data which doesn't have a valid time units. Outputs NuDatStrip3.txt
## Includes reference to the headers 'Name'
## LOL as usual this should be combined with the function above!!!

LT = ['s', 'ms', 'us', 'ns', 'ps', 'fs', 'as', 'zs', 'ys', 'm', 'h', 'd', 'y', 'ky', 'My', 'Gy', 'Ty', 'Py', 'Ey' 'Name']

with open('NudatStrip2.txt') as oldfile, open('NudatStrip3.txt', 'w') as newfile:
    for line in oldfile:
        clean = False
        for word in LT:
            if word in line:
                clean = True
        if clean == True:
            newfile.write(line)

## Splits the file to give file with nuclides and half-life data

fin = open("NudatStrip3.txt", "rt")
fout = open("NudatLife.txt", "wt")

for line in fin:
#        if len(line) > 10:
    fout.write(line[:37] + '\n')

fin.close()
fout.close()

## Splits the file to give file with only the decay modes

fin = open("NudatStrip3.txt", "rt")
fout = open("NudatDecay.txt", "wt")

for line in fin:
#   if len(line) > 10:
    fout.write(line[:18] + line[38:])

fin.close()
fout.close()

## Strips out Whitespace and replaces with ',' and replaces the carriage returns. Writes a file NudatStrip.txt which has the new data.
## Should really get combined with the function above

fin = open("NudatLife.txt", "rt")
fout = open("NudatLife2.txt", "wt")

for line in fin:
      fout.write(re.sub(' +', '\t', line).strip() + "\n")
fin.close()
fout.close()


## Imports fixed width delimited txt and outputs Nudat.csv

#import pandas as pd
#ds2 = pd.read_fwf('NudatStrip3.txt', widths=[4,7,7,8,3,8,80])
#ds2.to_csv('Nudat.csv')

## Uses pandas module to convert to csv

print(open('NudatLife2.txt').read())

import pandas as pd
df = pd.read_csv('NudatLife2.txt', delimiter='\t')
df.to_csv('NuDatLife2.csv')


#import csv
#csv.register_dialect('piper', delimiter=' ', quoting=csv.QUOTE_NONE)

#with open("NudatStrip3.txt", "rb") as csvfile:
#    for row in csv.DictReader(csvfile, dialect='piper'):
 #       print(row[1])


## Trial csv writer

with open("NudatClean.txt") as f:
    text=f.readlines()

## This is a csv importer taken from stackoverflow answer

with open("NudatLife2.txt") as f:
    text=f.readlines()

import csv
with open('dat2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in text:
        l=i.split('\t')
        row=[]
        for a in l:
            if a!='':
                row.append(a)
        print(row)
        writer.writerow(row)

