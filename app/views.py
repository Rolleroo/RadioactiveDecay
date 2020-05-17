from app import app
from flask import render_template, request
from app.businesslogic.BatemanDecay import bateman_trial
from app.businesslogic.DecayChain import Generator
from app.businesslogic.TestEnd import TestEnd
from app.businesslogic.BatemanMulti import BatemanMulti
from app.businesslogic.OutputFormat import OutputFormat
# from app.businesslogic.MeasurementUnit import Concentration
# from app.businesslogic.MeasurementUnit import Time
# from pint import UnitRegistry


@app.route('/')
def index():
    return render_template("public/index.html")



@app.route("/input", methods=["GET", "POST"])
def input():

    if request.method == "POST":

        input = request.form


        user_time = float(input["time"])
        user_tunit = str(input["tunit"])
        user_aunit = str(input["aunit"])

        # bateman_results = BatemanMulti(dict_input, user_time, user_tunit, user_aunit)

        chain_generator = Generator()

        bateman_results = {}

        for key, value1 in input.items():
            if key[0:8] == "activity":
                nuclide_id = "nuclide" + str(key[8])
                user_nuclide = input[str(nuclide_id)]
                user_activity = float(value1)
                result = bateman_trial(user_nuclide, user_time, user_tunit, user_activity, user_aunit)

                for nuclide, value2 in result.items():
                    if not bateman_results.get(nuclide):
                         bateman_results[nuclide] = 0
                    bateman_results[nuclide] += float(value2)


        output_result = OutputFormat(bateman_results, user_aunit)


        return render_template("public/output.html", result1=output_result, aunit=user_aunit)

    return render_template("public/input.html")

@app.route('/input2', methods=["GET", "POST"])
def input2():

    if request.method == "POST":
        ## sets the flask post to input
        input = request.form

        ## Grabs the user input and renames
        user_time = float(input["time"])
        user_tunit = str(input["tunit"])
        user_aunit = str(input["aunit"])

        ## Cleans up the text input from the user for input to BatemanMulti
        dict_input = TestEnd(input["test"])

        ## runs the user input text through bateman multinuclide run.
        bateman_results = BatemanMulti(dict_input, user_time, user_tunit, user_aunit)

        ## formats for return to flask and the webpage
        output_result = OutputFormat(bateman_results, user_aunit)


        return render_template("public/output.html", result1=output_result, aunit=user_aunit)

    return render_template("public/input2.html")

# @app.route("/about")
# def about():
#     return """
#     <h1 style='color: red;'>I'm a red H1 heading!</h1>
#     <p>This is a lovely little paragraph</p>
#     <code>Flask is <em>awesome</em></code>
#     """

