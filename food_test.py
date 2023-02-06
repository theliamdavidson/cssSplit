from food_test_definitions import Food_Test_Definition

class Food_Test(Food_Test_Definition):
    def __init__(self):
        super().__init__()
    
    def store_bvg2_value(self, value_input):
        for values in value_input:
            for index, vessels in enumerate(self.vessel_bvg2_values):
                if vessels[self.test_version] == None:
                    self.vessel_bvg2_values[index][self.test_version] = values[1]
                    self.vessel_bvg2s.append(values)

