from app import app
from flask import render_template, request
from app.businesslogic.BatemanDecay import bateman_trial
from app.businesslogic.FormatInput import FormatInput
from app.businesslogic.BatemanMulti import BatemanMulti
from app.businesslogic.OutputFormat import OutputFormat


@app.route('/')
def index():
    return render_template("public/index.html")



@app.route("/input", methods=["GET", "POST"])
def input():

## this is the single decay chaing site. It inputs only one nuclide and associated data

    if request.method == "POST":

        input = request.form

        user_time = float(input["time"])
        user_tunit = str(input["tunit"])
        user_aunit = str(input["aunit"])

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

## This is the multi nuclide calculator and inputs a tab separated data

    if request.method == "POST":
        ## sets the flask post to input
        input = request.form

        ## Grabs the user input and renames
        user_time = float(input["time"])
        user_tunit = str(input["tunit"])
        user_aunit = str(input["aunit"])

        user_nuc_conc = input["test"]

        # Cleans up empty spaces and formats for splits to dictionary for bateman
        try:
            dict_input = FormatInput(user_nuc_conc)
        except ValueError:
            error1 = "Please reformat your input."
            error2 = "An example syntax is shown below"
            return render_template("public/input2.html", error1=error1, error2=error2)

        ## runs the user input text through bateman multinuclide run.
        bateman_results = BatemanMulti(dict_input, user_time, user_tunit, user_aunit)

        ## formats for return to flask and the webpage
        output_result = OutputFormat(bateman_results, user_aunit)


        return render_template("public/output.html", result1=output_result, aunit=user_aunit)

    return render_template("public/input2.html")
