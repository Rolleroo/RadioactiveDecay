from app import app
from flask import render_template, request
from app.businesslogic.BatemanDecay import bateman_trial
from app.businesslogic.DecayChain import Generator
from app.businesslogic.MeasurementUnit import Concentration
from app.businesslogic.MeasurementUnit import Time
from pint import UnitRegistry

@app.route('/')
def index():
    return render_template("public/index.html")



@app.route("/input", methods=["GET", "POST"])
def input():

    if request.method == "POST":

        input = request.form

        user_nuclide1 = str(input["nuclide1"])
        user_nuclide2 = str(input["nuclide2"])
        user_time = float(input["time"])
        user_tunit = str(input["tunit"])
        user_aunit = str(input["aunit"])
        user_activity1 = float(input["activity1"])

        if not input["activity2"]:
            result1 = bateman_trial(user_nuclide1, user_time, user_tunit, user_activity1, user_aunit)
            result2 = bateman_trial(user_nuclide2, user_time, user_tunit, 0, user_aunit)

        else:
            user_activity2 = float(input["activity2"])
            result1 = bateman_trial(user_nuclide1, user_time, user_tunit, user_activity1, user_aunit)
            result2 = bateman_trial(user_nuclide2, user_time, user_tunit, user_activity2, user_aunit)

        chain_generator = Generator()

        # chains = chain_generator.get_for_nuclide_name(user_nuclide1)

        for nuclide, value in result2.items():
            print(nuclide, value)
            if not result1.get(nuclide):
                 result1[nuclide] = 0
            result1[nuclide] += float(value)

        print(result1)

        output_result = {}

        for nuclide_name, f_nuc_conc in result1.items():
            nuclide = chain_generator.nuclides_dict.get(nuclide_name)
            other_data = [format(f_nuc_conc,'.4g'),
                       user_aunit,
                       nuclide.halflife.value,
                       nuclide.halflife.unit
                          ]

            result = {'name' : nuclide_name, other_data}
            output_result.update(result)
        print(output_result)

        return render_template("public/output.html", result1=output_result, aunit=user_aunit)

    return render_template("public/input.html")

# @app.route("/about")
# def about():
#     return """
#     <h1 style='color: red;'>I'm a red H1 heading!</h1>
#     <p>This is a lovely little paragraph</p>
#     <code>Flask is <em>awesome</em></code>
#     """

