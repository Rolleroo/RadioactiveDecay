from app.businesslogic.BatemanDecay import bateman_trial

def BatemanMulti(dict_input, user_time, user_tunit, user_aunit):
    results = {}

    inputs = dict_input
    for nuclide, activity in inputs.items():
        user_nuclide = str(nuclide)
        user_activity = float(activity)
        result = bateman_trial(user_nuclide, user_time, user_tunit, user_activity, user_aunit)
        for nuclide, value2 in result.items():
            if not results.get(nuclide):
                results[nuclide] = 0
            results[nuclide] += float(value2)
    return results
