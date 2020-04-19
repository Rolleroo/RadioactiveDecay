from .DecayCalculationResult import DecayCalculationResult
from .DecayCalculationRequest import DecayCalculationRequest
from .MeasurementUnit import Concentration
from .MeasurementUnit import Halflife
from .MeasurementUnit import Time
from .Nuclide import Nuclide

class Decay:
    def __init__(
        self, 
        decay_calculation_request: DecayCalculationRequest
    ):
        self.decay_calculation_request = decay_calculation_request

    def calculate(self) -> [DecayCalculationResult]:
        result = []

        target_time = Time(
            value=self.decay_calculation_request.target_time_value,
            unit=self.decay_calculation_request.target_time_unit
        )

        for measurement in self.decay_calculation_request.measurements:
            nuclide = Nuclide(
                name=measurement.get('nuclide_name'),
                concentration=Concentration(
                    value=measurement.get('concentration_value'),
                    unit=measurement.get('concentration_unit')
                ),
                halflife=Halflife(
                    value=1,
                    unit="ky"
                )
            )

            calculated_concentration = nuclide.calculate_concentration_at_time(target_time)

            result.append(
                DecayCalculationResult(
                    nuclide=nuclide,
                    concentration=calculated_concentration,
                    time=target_time
                )
            )

        return result
