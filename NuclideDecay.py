## Imports the class Nuclide from the NuclideClass.py

#from NuclideClass import Nuclide

## Brings in the Unit Registry from the pint module. The pints module needs to be added in the "project interprer"
## in Pycharm or using pip. This deals automatically with any units added.
## This adds the definitions for years as 'y' as well as 'yr' from mydef.txt which is stored in the proj folder

from pint import UnitRegistry
ureg = UnitRegistry()
ureg.load_definitions('my_def.txt')

## Sets these values to quantites used by pint
A_ = ureg.Quantity
B_ = ureg.Quantity
C_ = ureg.Quantity

## This is the user input section

## This script constructs the quantity for halflife to make sure it is valid. If not it quits and drops an error.

common_name = input("Common Name: ")

try:
        half_life = float(input("Enter the halflife of the nuclide: "))
        hl_units = input("Half-life units i.e. s, h, d, m, y etc: ")
        full_HL = C_(half_life, hl_units)
except:
        print("The half-life input is not recognised, maybe you entered incorrect units, please try again.")

else:
        try:
            conc = float(input("Initial activity: "))
            conc_unit = input("Activity units: ")
        except:
            print("The activity information is not correct did you enter a number or the correct units?")
        else:

            time = input("Decay time: ")
            time_unit = input("Units of time: ")

            ## These will be used in a later version which will calculate the decay type and chain

            # decay_mode1 = input("Decay Mode 1 i.e. B-, B+, A, IC, IT: ")
            # mode1_fraction = input("Decay Mode 1 fraction i.e. 1 = 100%, 0.5 = 50%:  ")
            # decay_mode2 = input("Decay Mode 2 i.e. B-, B+, A, IC, IT. If none type N/A: ")
            # mode2_fraction = input("Decay Mode 2 fraction i.e. 1 = 100%, 0.5 = 50%. If none type 0: ")
            # protons = input("Number of Protons: ")
            # mass = input("Atomic Mass: ")
            # stable = input("Stable: ")

## Converts the time units to quantities as per pint module
            full_time = B_(float(time), time_unit)

## Changes the decay time and halflife to be seconds
            full_HL.ito_base_units()
            full_time.ito_base_units()

## Calculates the ratio of decay time and halflife
## This uses the magnitude so the output is dimensionless
            t_over_h = float(full_time.magnitude) / float(full_HL.magnitude)

## Calculates the amount of nuclide left after the time.
## As per https://en.wikipedia.org/wiki/Half-life
            finalconc = A_(((float(conc) * 0.5 ** (float(t_over_h)))), conc_unit)

## Prints the final concentration at time t.
            print("The final concentration of " + common_name + " after " + str(time) + " " + str(time_unit) + " =")
            print(finalconc)
