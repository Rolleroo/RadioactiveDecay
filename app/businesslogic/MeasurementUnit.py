## Brings in the Unit Registry from the pint module.
## This adds the definitions for years as 'y' as well as 'yr' from mydef.txt which is stored in the proj folder
from pint import UnitRegistry
ureg = UnitRegistry()
ureg.define('ky = yr * 1000 = [time]')
ureg.define('My = yr * 1000000 = [time]')
ureg.define('Gy = yr * 1000000000 = [time]')
ureg.define('Ty = yr * 1000000000000 = [time]')
ureg.define('Py = yr * 1000000000000000 = [time]')
ureg.define('y  = yr = [time]')
ureg.define('m  = second * 60 = [time]')
ureg.define('h  = second * 3600 = [time]')

class Base:
    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit
        self.quantity = ureg.Quantity(value, unit)

    def __json__(self, request):
        return {
            'value': self.value,
            'unit': self.unit
        }

class Concentration(Base):
    def __init__(self, value, unit):
        super().__init__(value, unit)

class Halflife(Base):
    def __init__(self, value, unit):
        super().__init__(value, unit)

class Time(Base):
    def __init__(self, value, unit):
        super().__init__(value, unit)
