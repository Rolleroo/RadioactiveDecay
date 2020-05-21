from app import app
from flask import render_template, request
from app.businesslogic.BatemanDecay import bateman_trial
from app.businesslogic.FormatInput import FormatInput
from app.businesslogic.BatemanMulti import BatemanMulti
from app.businesslogic.OutputFormat import OutputFormat
import re

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
        user_nuclide = str(input["nuclide1"])
        user_activity = float(input["activity1"])

        bateman_results = {}

        atomic_mass = int("".join(filter(str.isdigit, user_nuclide)))
        element_regex = r"[a-zA-Z]{1,2}"
        element = re.findall(element_regex, user_nuclide)[0]
        element_f = element[0].upper() + element[1:]
        nuclide_out = str(element_f) + "-" + str(atomic_mass)

        result = bateman_trial(nuclide_out, user_time, user_tunit, user_activity, user_aunit)

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
            error3 = "Error"
            return render_template("public/input2.html", error1=error1, error2=error2, error3=error3)

        ## runs the user input text through bateman multinuclide run.
        bateman_results = BatemanMulti(dict_input, user_time, user_tunit, user_aunit)

        ## formats for return to flask and the webpage
        output_result = OutputFormat(bateman_results, user_aunit)


        return render_template("public/output.html", result1=output_result, aunit=user_aunit)

    return render_template("public/input2.html")
