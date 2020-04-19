from .Nuclide import Nuclide
from .MeasurementUnit import Concentration
from .MeasurementUnit import Time

class DecayCalculationResult:
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