import pyramid.httpexceptions as exc
from cornice import Service
from app.businesslogic.DecayCalculation import Calculator
from app.businesslogic.DecayCalculation import Request

decay_calculation = Service(
    name='decay_calculation',
    description='Calculate decay',
    path='/decay/calculate'
)

decay_calculator = Calculator()

@decay_calculation.post() # pylint: disable=no-member
def decay_calculation_post(request):
    if not request.json_body:
        raise exc.exception_response(404) 
    
    decay_calculation_request = Request(request.json_body)
    
    result = decay_calculator.calculate(
        decay_calculation_request=decay_calculation_request
    )

    return {
        "results": result
    }