from typing import List

from app.businesslogic.MeasurementUnit import Concentration
from app.businesslogic.MeasurementUnit import Halflife
from app.businesslogic.MeasurementUnit import Time

class Nuclide:
    def __init__(
        self, 
        name: str = None, 
        radioactive: bool = True,
        halflife_value: float = None,
        halflife_unit: str = None,
        decay_mode: str = None,
        daughter_nuclide_names: List[str] = [],
        daughter_nuclide_ratios:  List[str] = []
    ):
        self.name = name
        self.radioactive = radioactive
        if halflife_value and halflife_unit:
            self.halflife = Halflife(halflife_value, halflife_unit)
        else:
            self.halflife = None
        self.decay_mode = decay_mode
        self.daughter_nuclide_names = daughter_nuclide_names
        self.daughter_nuclide_ratios = daughter_nuclide_ratios

    def __json__(self, request):
        return {
            'name': self.name,
            'radioactive': self.radioactive,
            'halflife': self.halflife,
            'decay_mode': self.decay_mode,
            'daughter_nuclide_names': self.daughter_nuclide_names,
            'daughter_nuclide_ratios': self.daughter_nuclide_ratios
        }
