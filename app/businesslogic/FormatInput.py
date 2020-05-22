## For thThis function removes extra carriage returns, formats the nuclides
# and splits the input whitespace (dict divide) and \r\n (next item)

import re
from app.businesslogic.NuclideFormatter import NuclideFormatter

def FormatInput(inputs):
    print(inputs)
    unformatted = str(inputs)
    ## Removes extra carriage returns from the beginning and end
    while unformatted[-2:] == "\r\n":
        unformatted = unformatted[0:-2]
    while unformatted[0:2] == "\r\n":
        unformatted = unformatted[2:]
    ## Splits the text based on space and return carriage.
    formatted = list(map(lambda x: re.split(r'\s+', x), re.split(r'\r\n+', unformatted)))


    outputs = {}
    ## Splits digits and text for nuclides and reassembles in format XY-123
    for values in formatted:
        nuclide = values[0]
        conc = float(values[1])
        nuclide_out = NuclideFormatter(nuclide)
        formatted = {nuclide_out: conc}
        print(formatted)
        for k in formatted.keys():
            outputs[k] = outputs.get(k,0) + formatted[k]

    return outputs

