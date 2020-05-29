# RadioactiveDecay
This is a working repository for a radioactive decay calculator website.

This is a python based program which uses a C++ based python module to calculate the decay of radioactivity over time.

A simple front end html is used to acquire user input.

Current configurations only run on Linux server and require C++ compiler such as gcc.

Git software, although not stricly necessary if ther repository is manually copied in.

To install:

Download the source code

    git clone https://github.com/Rolleroo/RadioactiveDecay.git

Setup a python environment

Change to app directory

    cd RadioactiveDecay

Setup up the Virtual Environment and activate it.

    python -m venv env
    
    source env/bin/activate

Update & Install Requirements

    pip install --upgrade pip
    pip install -r /path/to/requirements.txt

Run the python app

    python run.py

## Data
* Radionuclide decay
Article: https://www.icrp.org/publication.asp?id=ICRP%20Publication%20107
Supplementary Data (ZIP file): https://journals.sagepub.com/doi/suppl/10.1177/ANIB_38_3
File used: ./ICRP-07.NDX (column names as per ./UserGuide.pdf - table on page 4)

## Thanks
With particular thanks to @bjodah for use of the batemaneq module (https://github.com/bjodah/batemaneq).


