import json
from prettyprinter import cpprint
from app.businesslogic.MeasurementUnit import Concentration
from app.businesslogic.MeasurementUnit import Halflife
from app.businesslogic.MeasurementUnit import Time
from app.businesslogic.Nuclide import Nuclide
from app.businesslogic.DecayChain import Generator


class Request:
    def __init__(self, request_dict):
        self.measurements = request_dict.get('measurements')
        self.target_time_value = request_dict.get('target_time_value')
        self.target_time_unit = request_dict.get('target_time_unit')

class Result:
    def __init__(self, nuclide: Nuclide, concentration: Concentration, time: Time):
        self.nuclide = nuclide
        self.concentration = concentration
        self.time = time

    def __json__(self, request):
        return {
            'nuclide': self.nuclide,
            'calculation': {
                'concentration': self.concentration,
                'time': self.time
            }
        }

class Calculator:
    def __init__(self):
        self.chain_generator = Generator()

    def calculate(self, decay_calculation_request: Request) -> [Result]:
        result = []

        target_time = Time(
            value=decay_calculation_request.target_time_value,
            unit=decay_calculation_request.target_time_unit
        )

        for measurement in decay_calculation_request.measurements:
            nuclide_name = measurement.get('nuclide_name')
            chains = self.chain_generator.get_for_nuclide_name(nuclide_name)
            chains_names_only = [
                chain.get_nuclide_names()
                for chain in chains
            ]

            print(json.dumps(chains_names_only, indent=4))

            initial_concentration = Concentration(
                value=measurement.get('concentration_value'),
                unit=measurement.get('concentration_unit')
            )

            # calculated_concentration = nuclide.calculate_concentration_at_time(initial_concentration, target_time)

            # result.append(
            #     Result(
            #         nuclide=nuclide,
            #         concentration=calculated_concentration,
            #         time=target_time
            #     )
            # )

        return result
