# RadioactiveDecay

## Getting Started

* Create a Python virtual environment:

    ```python3 *m venv env```

* Upgrade packaging tools:

    ```env/bin/pip install **upgrade pip setuptools```

* Install the project in editable mode with its testing requirements:

    ```env/bin/pip install -e ".[testing]"```

* Run your project's tests:

    ```env/bin/pytest```

* Run your project:

    ```env/bin/pserve development.ini```

## Data
* Radionuclide decay
Article: https://www.icrp.org/publication.asp?id=ICRP%20Publication%20107
Supplementary Data (ZIP file): https://journals.sagepub.com/doi/suppl/10.1177/ANIB_38_3
File used: ./ICRP-07.NDX (column names as per ./UserGuide.pdf - table on page 4)