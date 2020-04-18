import pyramid.httpexceptions as exc
from cornice import Service
from ..businesslogic.Decay import Decay
from ..businesslogic.DecayCalculationRequest import DecayCalculationRequest

decay_calculation = Service(
    name='decay_calculation',
    description='Calculate decay',
    path='/decay/calculate'
)

@decay_calculation.post() # pylint: disable=no-member
def decay_calculation_post(request):
    if not request.json_body:
        raise exc.exception_response(404) 
    
    decay_calculation_request = DecayCalculationRequest(request.json_body)

    decay = Decay(
        decay_calculation_request=decay_calculation_request
    )
    
    result = decay.calculate()

    return {
        "results": result
    }