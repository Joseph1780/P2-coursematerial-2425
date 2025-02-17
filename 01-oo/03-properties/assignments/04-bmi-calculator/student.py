class BMICalculator :
    def __init__(self, weight_in_kg: float, height_in_m: float):
        self.weight_in_kg = weight_in_kg
        self.height_in_m = height_in_m

    @property
    def get_bmi(self):
        