## This script will recombine the decay chains.
## Format of incoming chain is in the format (NuclidEA, NuclidEB........ , fraction)
## Fraction will be the multiplication of all branching factors for each branch taken
## i.e. if the chain branches 3 times and the branching factors are 0.5 each time the final factor will be 0.5*0.5*0.5 
## or 0.125

from app.businesslogic.Nuclide import Nuclide
from MeasurementUnit import Halflife
from MeasurementUnit import Concentration
from pint import UnitRegistry
ureg = UnitRegistry()

## Trial data
## 4 chains 
## A > B > C > D > E
## A > F > C > D > E
## A > B > C > D > G
## A > F > C > D > G
## Assumes all data will have been converted into Bq in BatemanDecay.py

hl_nuclideA = Halflife(7.04E+08, "yr").quantity  # U-235
hl_nuclideB = Halflife(25.52, "hour").quantity  # Th-231 trial
hl_nuclideC = Halflife(32760.0, "yr").quantity  # Pa-231 trial
hl_nuclideD = Halflife(21.772, "yr").quantity # Ac-227 trial
hl_nuclideE = Halflife(16.68, "d").quantity  # Th-227 trial
hl_nuclideF = Halflife(22.0, "minute").quantity  # Fr-223 trial
hl_nuclideG = Halflife(11.43, "d").quantity  # Ra-223 trial



nuclideA_conc = Concentration(0.5, "Bq")
nuclideBA_conc = Concentration(0.5, "Bq")
nuclideBB_conc = Concentration(0.5, "Bq")
nuclideCA_conc = Concentration(0.5, "Bq")
nuclideCB_conc = Concentration(0.5, "Bq")
nuclideCC_conc = Concentration(0.5, "Bq")
nuclideCD_conc = Concentration(0.5, "Bq")
nuclideDA_conc = Concentration(0.5, "Bq")
nuclideDB_conc = Concentration(0.5, "Bq")
nuclideDC_conc = Concentration(0.5, "Bq")
nuclideDD_conc = Concentration(0.5, "Bq")
nuclideEA_conc = Concentration(0.5, "Bq")
nuclideEB_conc = Concentration(0.5, "Bq")
nuclideFA_conc = Concentration(0.5, "Bq")
nuclideFB_conc = Concentration(0.5, "Bq")
nuclideGA_conc = Concentration(0.5, "Bq")
nuclideGB_conc = Concentration(0.5, "Bq")


nuclideA = Nuclide("A", hl_nuclideA, nuclideA_conc)
nuclideBA = Nuclide("B", hl_nuclideB, nuclideBA_conc)
nuclideBB = Nuclide("B", hl_nuclideB, nuclideBB_conc)
nuclideCA = Nuclide("C", hl_nuclideC, nuclideCA_conc)
nuclideCB = Nuclide("C", hl_nuclideC, nuclideCB_conc)
nuclideCC = Nuclide("C", hl_nuclideC, nuclideCC_conc)
nuclideCD = Nuclide("C", hl_nuclideC, nuclideCD_conc)
nuclideDA = Nuclide("D", hl_nuclideD, nuclideDA_conc)
nuclideDB = Nuclide("D", hl_nuclideD, nuclideDB_conc)
nuclideDC = Nuclide("D", hl_nuclideD, nuclideDC_conc)
nuclideDD = Nuclide("D", hl_nuclideD, nuclideDD_conc)
nuclideEA = Nuclide("E", hl_nuclideE, nuclideEA_conc)
nuclideEB = Nuclide("E", hl_nuclideE, nuclideEB_conc)
nuclideFA = Nuclide("F", hl_nuclideF, nuclideFA_conc)
nuclideFB = Nuclide("F", hl_nuclideF, nuclideFB_conc)
nuclideGA = Nuclide("G", hl_nuclideG, nuclideGA_conc)
nuclideGB = Nuclide("G", hl_nuclideG, nuclideGB_conc)


fraction1 = 0.1
fraction2 = 0.01
fraction3 = 0.001
fraction4 = 0.0001

chain1 = [nuclideA, nuclideBA, nuclideCA, nuclideDA, nuclideEA, fraction1]
chain2 = [nuclideA, nuclideFA, nuclideCB, nuclideDB, nuclideEB, fraction2]
chain3 = [nuclideA, nuclideBB, nuclideCC, nuclideDC, nuclideGA, fraction3]
chain4 = [nuclideA, nuclideFB, nuclideCD, nuclideDD, nuclideGB, fraction4]

## Defines a class to help count the chains. Not sure this is optimal but every chain will be passed into the
## class.

class Chain:

    number_of_chains = 0

    def __init__(self, chain_ID):
        self.chain_ID = chain_ID
        Chain.number_of_chains += 1

Chain1 = Chain(chain1)
Chain2 = Chain(chain2)
Chain3 = Chain(chain3)
Chain4 = Chain(chain4)

## The chains will be stripped down to component parts to allow construction and calculation.

unique_list = []
name_list = []
conc_list = []
hl_list = []
f_conc = []

def name_strip ( input ):
    for i in input[:-1]:
        name_list.append(i.name)
        conc_list.append(i.concentration.value * input[-1])
        if i.name not in unique_list:
            unique_list.append(i.name)
            hl_list.append(i.halflife)

## Cycles through each chain and carries out name_strip on them.

d = 1
while d <= Chain.number_of_chains:
    v = globals()["chain" + str(d)]
    name_strip(v)
    d += 1

## Searches through the each chain for entries in the unique radionuclide list
#= , determines the concentration, multiplies it by the fraction of that chain and totals them in f_conc
## Then recombines into the Nuclide class.

c = 0
w = 0

for k in unique_list:
    w = 0
    for n, i in enumerate(name_list):
        if i == k:
            w += float(conc_list[n])

    z = Nuclide(k, hl_list[c], Concentration(w, "Bq"))
    f_conc.append(z)
    c += 1

## For testing prints out the final results.

for i in f_conc:
    s = i
    print(s.concentration.value)
