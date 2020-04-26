## The example equation from Batemaneq GitHub page

## Requires the following packages numpy, cython, scipy.
## Nuclides with half lifes of less than one hour are dropped automatically in batemaneq module.
## Bateman equation uses concentrations rather than activity (Bq).
## The activity therefore has to be converted to a concentration for calculation.

import sys
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

decay_time = Time(0.1, "yr").quantity
hl_nuclide1 = Halflife(4.468e9, "yr").quantity
nuclide1_conc = Concentration(10000, "Bq").quantity
nuclide1 = Nuclide("U-238", hl_nuclide1, nuclide1_conc)


## Converts the Bq of nuclide 1 into moles
real_nuclide_conc = (nuclide1_conc.magnitude * hl_nuclide1.magnitude / ACT_CONV)

## Test data for the calculations

hl_nuclide2 = Halflife(24.1, "d").quantity  # Th234 trial
hl_nuclide3 = Halflife(2.455e5, "yr").quantity  # U234 trial
hl_nuclide4 = Halflife(7.538e4, "yr").quantity # Th230 trial
hl_nuclide5 = Halflife(1600, "yr").quantity  # Ra226 trial
hl_nuclide6 = Halflife(3.823, "d").quantity  # Rn 222 trial
hl_nuclide7 = Halflife(3.05, "min").quantity  # Po 218 trial
hl_nuclide8 = Halflife(26, ",min").quantity  # Pb 214 trial
hl_nuclide9 = Halflife(19.9, "min").quantity  # Bi 214 trial
hl_nuclide10 = Halflife(160, "usec").quantity  # Po 214 trial
hl_nuclide11 = Halflife(22.26, "y").quantity  # Pb 210 trial

## Assumed format for output from decay chain
decay_chain = (hl_nuclide1, hl_nuclide2, hl_nuclide3, hl_nuclide4, hl_nuclide5, hl_nuclide6, hl_nuclide7,
               hl_nuclide8, hl_nuclide9, hl_nuclide10, hl_nuclide11)

## This sections formats for inputt to batemaneq module and carries out calculation through batemaneq.
## Initial radionuclide concentration is set to 1 all others are zero

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

## Converts the results output to final activity in Bq
final_act = []
z = 0
for i in result:
    x = i * (ACT_CONV / Thalf[z]) * real_nuclide_conc
    y = x * ureg.Bq
    final_act.append(y)
    z += 1

## For testing, outputs the final_act in Bq
for x in final_act:
    print(x)


