from app.businesslogic.DecayChain import Generator
from app.businesslogic.MeasurementUnit import Concentration
from app.businesslogic.MeasurementUnit import Time

## Bateman equation calculator from module
from batemaneq import bateman_parent

from math import log as ln # required for bateman module to function

# Unit handling module
from pint import UnitRegistry
ureg = UnitRegistry()


def bateman_trial(nuclide, time, tunit, conc, aunit):

    chain_generator = Generator()

    nuclide_name = nuclide
    concentration_value = conc
    concentration_unit = aunit
    decay_time = Time(time, tunit).quantity

    # start process of calculating stuff
    concentration = Concentration(
        value=concentration_value,
        unit=concentration_unit
    )

    # generate the decay chains for the supplied nuclide name
    chains = chain_generator.get_for_nuclide_name(nuclide_name)

    ## opens a final results list
    final_result = {}

    output_result = {}

    ## loop over decay chains and calculate
    for idx, chain in enumerate(chains):

        Thalf = []

        for item in chain.items:
            nuclide = item.nuclide
            ratio = item.ratio
            halflife = item.nuclide.halflife

            ## Used for testing, prints out each decay chain
            # radioactive = item.nuclide.radioactive
            # concentration = item.concentration
            # print(
            #     'Nuclide name:', nuclide.name,
            #     'Radioactive:', radioactive,
            #     'Decay ratio:', ratio,
            #     'Halflife:', halflife.quantity if halflife else None,
            #     'Concentration:', concentration
            # )

            ## Builds the halflife chain for input into bateman, drops stable isotopes.
            if item.nuclide.halflife != None:
                x = item.nuclide.halflife.quantity
                x.ito(ureg.years)
                Thalf.append(x.magnitude)

        ## Runs results through bateman module.
        output_items = bateman_parent([ln(2) / x for x in Thalf], decay_time.magnitude)

        ## Converts the results output to final activity concentration units and appends them to final_result dicionary

        for idx, output_item in enumerate(output_items):
            nuclide = chain.items[idx].nuclide
            if not final_result.get(nuclide.name):
                final_result[nuclide.name] = 0
            final_conc = output_item * (Thalf[0] / Thalf[idx]) * concentration_value
            relative_conc = Concentration(final_conc * chain.ratio, concentration_unit)

            final_result[nuclide.name] += float(relative_conc.value)


    return final_result

