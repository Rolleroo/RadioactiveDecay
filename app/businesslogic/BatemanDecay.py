## The example equation from Batemaneq GitHub page

## Requires the following packages numpy, cython, scipy.
## Nuclides with half lifes of less than one hour are dropped automatically in batemaneq module.
## Bateman equation uses concentrations rather than activity (Bq).
## The activity therefore has to be converted to a concentration for calculation.

# import sys
from pint import UnitRegistry
ureg = UnitRegistry()

from batemaneq import bateman_parent
from math import log as ln # required for bateman module to function
from app.businesslogic.Nuclide import Nuclide
from MeasurementUnit import Time
from MeasurementUnit import Halflife
from MeasurementUnit import Concentration

# Calculates a constant which converts Bq etc to concentration.
AVOGADRO_NUMBER = 6.02214076e23
ACT_CONV  = (AVOGADRO_NUMBER * ln(2)) / 24 / 365 / 60 / 60

## User input

decay_time = Time(1, "yr").quantity
hl_nuclide1 = Halflife(7.04E+08, "yr").quantity
nuclide1_conc = Concentration(10000, "Bq").quantity.to(ureg.Bq)
nuclide1 = Nuclide("U-235", hl_nuclide1, nuclide1_conc)
zero_nuclide_conc = Concentration(0, "Bq").quantity

## Converts the Bq of nuclide 1 into moles
real_nuclide_conc = (nuclide1_conc.magnitude * hl_nuclide1.magnitude / ACT_CONV)

## Test data for the calculations
## Requires a lookup function here to look up the halflife of the nuclides in the list

hl_nuclide2 = Halflife(25.52, "hour").quantity  # Th-231 trial
hl_nuclide3 = Halflife(32760.0, "yr").quantity  # Pa-231 trial
hl_nuclide4 = Halflife(21.772, "yr").quantity # Ac-227 trial
hl_nuclide5 = Halflife(16.68, "d").quantity  # Th-227 trial
hl_nuclide6 = Halflife(22.0, "minute").quantity  # Fr-223 trial
hl_nuclide7 = Halflife(11.43, "d").quantity  # Ra-223 trial
hl_nuclide8 = Halflife(56, ",sec").quantity  # At-219 trial
hl_nuclide9 = Halflife(3.96, "sec").quantity  # Rn-219 trial


nuclide2 = Nuclide("Th-231", hl_nuclide2, zero_nuclide_conc)
nuclide3 = Nuclide("Pa-231", hl_nuclide3, zero_nuclide_conc)
nuclide4 = Nuclide("Ac-227", hl_nuclide4, zero_nuclide_conc)
nuclide5 = Nuclide("Th-227", hl_nuclide5, zero_nuclide_conc)
nuclide6 = Nuclide("Fr-223", hl_nuclide6, zero_nuclide_conc)
nuclide7 = Nuclide("Ra-223", hl_nuclide7, zero_nuclide_conc)
nuclide8 = Nuclide("At-219", hl_nuclide8, zero_nuclide_conc)
nuclide9 = Nuclide("Rn-219", hl_nuclide9, zero_nuclide_conc)

## This is the fractional contribution of the chain. Added for completeness
fraction = 1

## It is assumed this will be the output format from the lookup tables.
chain = (nuclide1, nuclide2, nuclide3, nuclide4, nuclide5,
         nuclide6, nuclide7, nuclide8, nuclide9, fraction)

## Creates the a list of the nuclide names and halflifes based on the order in chain
decay_chain = []
for i in chain[:-1]:
    hl = i
    decay_chain.append(hl.halflife)

name_chain = []
for i in chain[:-1]:
    nuc_name = i
    name_chain.append(nuc_name.name)

## This sections formats for inputt to batemaneq module and carries out calculation through batemaneq.
## Initial radionuclide concentration is set to 1 all zeros are zero
## time units are converted to years with the to(ureg.year) function

Thalf = []

for x in decay_chain:
    x.to(ureg.year)
    Thalf.append(x.magnitude)

# ## Determines if consecutive HL values are too similar and prints an error. R
# ## Removed for now, errors are dependent on relationship to all half-lifes!!!
# for x, y in zip(Thalf, Thalf[1:]):
#     if x == y:
#         print("Consecutive half-life values are equal. This does not compute please check and try again\n")
#         sys.exit(1)
#
#     if  0.2 <= x/y <= 5:
#         print("Consecutive half-life values are very similar. "
#               "The Bateman equation struggles with these values and there"
#               " may be some error in the final results.\nPlease check the results\n")

## Runs the bateman decay and outputs the results
result = bateman_parent([ln(2)/x for x in Thalf], decay_time.magnitude) # ignores halflifes less than 1 day

## Converts the results output to final activity in Bq and appends them to final_act list
final_act = []
a = 0
for i in result:
    w = i * (ACT_CONV / Thalf[a]) * real_nuclide_conc
    q = Concentration(w, "Bq").quantity
    z = Nuclide(name_chain[a], decay_chain[a], q)
    final_act.append(z)
    a += 1

final_act.append(fraction)


## Test which outputs the contents of final_act
for i in final_act[:-1]:
    testnuc = i
    print(testnuc.concentration)

print(result)

