from .Nuclide import Nuclide
from .MeasurementUnit import Activity
from .MeasurementUnit import Time

class DecayCalculationResult:
    def __init__(self, nuclide: Nuclide, activity: Activity, time: Time):
        self.nuclide = nuclide
        self.activity = activity
        self.time = time

    def __json__(self, request):
        return {
            'nuclide': self.nuclide,
            'calculation': {
                'activity': self.activity,
                'time': self.time
            }
        }