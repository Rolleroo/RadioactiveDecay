import re

def NuclideFormatter(nuclide):
    user_nuclide = nuclide

    is_m = (user_nuclide.strip()[-1] == "m")

    atomic_mass = int("".join(filter(str.isdigit, user_nuclide)))
    element_regex = r"[a-zA-Z]{1,2}"
    element = re.findall(element_regex, user_nuclide)[0]
    element_f = element[0].upper() + element[1:]
    nuclide_out = str(element_f) + "-" + str(atomic_mass) + ('m' if is_m else '')
    return nuclide_out