import json
from app.businesslogic.DecayChain import Generator
from app.businesslogic.MeasurementUnit import Concentration
from app.businesslogic.MeasurementUnit import Time
from app.businesslogic.Nuclide import Nuclide
from app.businesslogic.DecayCalculation import Result
from batemaneq import bateman_parent
from math import log as ln # required for bateman module to function
from pint import UnitRegistry
ureg = UnitRegistry()

chain_generator = Generator()

# user supplied
nuclide_name = 'U-238'
concentration_value = 30
concentration_unit = 'Bq'
decay_time = Time(421, "yr").quantity

# start process of calculating stuff
concentration = Concentration(
    value=concentration_value,
    unit=concentration_unit
)

# generate the decay chains for the supplied nuclide name
chains = chain_generator.get_for_nuclide_name(nuclide_name)

## opens a final results list
f_result = {}

# loop over decay chains and calculate
for idx, chain in enumerate(chains):
    # add your bateman calculation somewhere here for each chain

    # code below simply prints the derived chains for information only
    
    # print('Chain number:', idx + 1)

    Thalf = []

    for item in chain.items:
        nuclide = item.nuclide
        radioactive = item.nuclide.radioactive
        ratio = item.ratio
        halflife = item.nuclide.halflife
        concentration = item.concentration
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
    output_items = bateman_parent([ln(2) / x for x in Thalf], decay_time.magnitude) # ignores halflifes less than 1 day

    ## Converts the results output to final activity concentration units and appends them to final_act list

    for idx, output_item in enumerate(output_items):
        nuclide = chain.items[idx].nuclide
        if not f_result.get(nuclide.name):
            f_result[nuclide.name] = 0
        w = output_item * (Thalf[0] / Thalf[idx]) * concentration_value
        q = Concentration(w * chain.ratio, concentration_unit)
        f_result[nuclide.name] += float(q.value)

for nuclide_name, total_conc in f_result.items():
    nuclide = chain_generator.nuclides_dict.get(nuclide_name)
    print(
            nuclide.name,"\t Halflife:  ",
            nuclide.halflife.value,
            nuclide.halflife.unit,
            "\t Final Concentration:  ",
            total_conc,
            concentration_unit
          )

