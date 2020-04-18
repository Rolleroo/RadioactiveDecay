class DecayCalculationRequest:
    def __init__(self, request_dict):
        self.activity_unit = request_dict.get('activity_unit')
        self.nuclide_measurements = request_dict.get('nuclide_measurements')
        self.target_time_value = request_dict.get('target_time_value')
        self.target_time_unit = request_dict.get('target_time_unit')