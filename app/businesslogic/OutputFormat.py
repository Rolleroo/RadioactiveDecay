from app.businesslogic.DecayChain import Generator

## This function formats the results into a dictionary {nuclide : [activity, activity unit, HL, HL unit]}
## This the format that flask needs to get this to run.

def OutputFormat(bateman_dict, user_aunit):
    chain_generator = Generator()
    output_result = {}
    for nuclide_name, f_nuc_conc in bateman_dict.items():
        nuclidess = chain_generator.nuclides_dict.get(nuclide_name)
        other_data = [format(f_nuc_conc, '.4g'),
                      user_aunit,
                      nuclidess.halflife.value,
                      nuclidess.halflife.unit
                      ]

        resultss = {nuclide_name: other_data}
        output_result.update(resultss)
        output_result = dict(sorted(output_result.items()))
    return output_result