## This function removes extra carriage returns, formats the nuclides
# and splits the input whitespace (dict divide) and \r\n (next item)

import re

def FormatInput(inputs):
    unformatted = str(inputs)
    ## Removes extra carriage returns from the beginning and end
    while unformatted[-2:] == "\r\n":
        unformatted = unformatted[0:-2]
    while unformatted[0:2] == "\r\n":
        unformatted = unformatted[2:]
    ## Splits the text based on space and return carriage.
    formatted = dict(map(lambda x: re.split(r'\s+', x), re.split(r'\r\n+', unformatted)))
    outputs = {}
    ## Splits digits and text for nuclides and reassembles in format XY-123
    for nuclide, values in formatted.items():
        atomic_mass = int("".join(filter(str.isdigit, nuclide)))
        element_regex = r"[a-zA-Z]{1,2}"
        element = re.findall(element_regex, nuclide)[0]
        element_f = element[0].upper() + element[1:]
        nuclide_out = str(element_f) + "-" + str(atomic_mass)
        formatted2 = {nuclide_out: values}
        outputs.update(formatted2)

    return outputs

