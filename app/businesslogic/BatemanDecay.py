## The example equation from Batemaneq GitHub page

## Requires the following packages numpy, cython, scipy, pytest.
## Nuclides with half lifes of less than one hour are dropped automatically in batemaneq module.
## Bateman equation uses concentrations rather than activity (Bq).
## The activity therefore has to be converted to a concentration for calculation.

from batemaneq import bateman_parent
from math import log as ln

d = 1./365  # Converts to days. Needs parsing through the pints module.
h = d/24    # Converts to years. Needs parsing through the pints module.

# Calculates a constant which converts Bq etc to concentration.
act_conv = (6.02214076e23 * ln(2)) / 24 / 365 / 60 / 60

## User input activity e.g. Bq or Bq/g.
## This is dimensionless, units added at the end.
user_activity = 1e9

hl_nuclide1 = 4.468e9 # U238 trial
hl_nuclide2 = 24.1 * d # Th234 trial
hl_nuclide3 = 2.445e5 # U234 trial
hl_nuclide4 = 7.54e4 # Th230 trial
hl_nuclide5 = 1600 # Ra226 trial
hl_nuclide6 = 3.823 * d # Rn 222 trial

decay_time = 100 # User input decay time in years

user_conc = user_activity* hl_nuclide1 / act_conv
print(user_conc) # prints out the concentration of the initial radionuclide in moles for testing.

## This sections formats for inputt to batemaneq module and carries out calculation through batemaneq.
## Initial radionuclide concentration is set to 1 all others are zero
Thalf = [hl_nuclide1, hl_nuclide2, hl_nuclide3, hl_nuclide4, hl_nuclide5, hl_nuclide6]
result = bateman_parent([ln(2)/x for x in Thalf], decay_time)
print(result)  # Outputs the results for testing

## The following equations convert the radionuclide concentrations to activity in the user
## units. The results are printed for test purposes.
act_nuclide1 = result[0] * (act_conv / hl_nuclide1) * user_conc # hl_nuclide must be in years
print(act_nuclide1)
act_nuclide2 = result[1] * (act_conv / hl_nuclide2) * user_conc # hl_nuclide must be in years
print(act_nuclide2)
act_nuclide3 = result[2] * (act_conv / hl_nuclide3) * user_conc # hl_nuclide must be in years
print(act_nuclide3)
act_nuclide4 = result[3] * (act_conv / hl_nuclide4) * user_conc # hl_nuclide must be in years
print(act_nuclide4)
act_nuclide5 = result[4] * (act_conv / hl_nuclide5) * user_conc # hl_nuclide must be in years
print(act_nuclide5)
act_nuclide6 = result[5] * (act_conv / hl_nuclide6) * user_conc # hl_nuclide must be in years
print(act_nuclide6)

