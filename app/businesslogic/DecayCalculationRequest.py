class DecayCalculationRequest:
    def __init__(self, request_dict):
        self.measurements = request_dict.get('measurements')
        self.target_time_value = request_dict.get('target_time_value')
        self.target_time_unit = request_dict.get('target_time_unit')