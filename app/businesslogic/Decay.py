from .DecayCalculationResult import DecayCalculationResult
from .DecayCalculationRequest import DecayCalculationRequest
from .MeasurementUnit import Activity
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

        for nuclide_measurement in self.decay_calculation_request.nuclide_measurements:
            nuclide = Nuclide(
                name=nuclide_measurement.get('name'),
                activity=Activity(
                    value=nuclide_measurement.get('activity_value'),
                    unit=self.decay_calculation_request.activity_unit
                ),
                halflife=Halflife(
                    value=1,
                    unit="ky"
                )
            )

            time = Time(
                value=3,
                unit="ky"
            )

            calculated_activity = nuclide.calculate_activity_at_time(time)

            result.append(
                DecayCalculationResult(
                    nuclide=nuclide,
                    activity=calculated_activity,
                    time=time
                )
            )

        return result
