from .MeasurementUnit import Activity
from .MeasurementUnit import Halflife
from .MeasurementUnit import Time

class Nuclide:
    def __init__(
        self, 
        name: str, 
        halflife: Halflife,
        activity: Activity
    ):
        self.name = name
        self.activity = activity
        self.halflife = halflife

    def __json__(self, request):
        return {
            'name': self.name,
            'activity': self.activity,
            'halflife': self.halflife
        }

    def calculate_activity_at_time(self, time: Time) -> Activity:
        full_HL = self.halflife.quantity
        full_time = time.quantity
        ## Changes the decay time and halflife to be seconds
        full_HL.ito_base_units()
        full_time.ito_base_units()

        ## These will be used in a later version which will calculate the decay type and chain

        # decay_mode1 = input("Decay Mode 1 i.e. B-, B+, A, IC, IT: ")
        # mode1_fraction = input("Decay Mode 1 fraction i.e. 1 = 100%, 0.5 = 50%:  ")
        # decay_mode2 = input("Decay Mode 2 i.e. B-, B+, A, IC, IT. If none type N/A: ")
        # mode2_fraction = input("Decay Mode 2 fraction i.e. 1 = 100%, 0.5 = 50%. If none type 0: ")
        # protons = input("Number of Protons: ")
        # mass = input("Atomic Mass: ")
        # stable = input("Stable: ")

        ## Calculates the ratio of decay time and halflife
        ## This uses the magnitude so the output is dimensionless
        t_over_h = float(full_time.magnitude) / float(full_HL.magnitude)

        ## Calculates the amount of nuclide left after the time.
        ## As per https://en.wikipedia.org/wiki/Half-life
        finalactivity = Activity(
            value=self.activity.value * 0.5 ** t_over_h,
            unit=self.activity.unit
        )

        return finalactivity
