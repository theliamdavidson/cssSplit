from food_test_definitions import Food_Test_Definition

class Food_Test(Food_Test_Definition):
    def __init__(self):
        super().__init__()
    
    def store_bvg2_value(self, value_input):
        for values in value_input:
            for index, vessels in enumerate(self.vessels_for_food_test):
                if vessels == values[0]:
                    self.vessel_bvg2_values[index][self.test_version] = values[1][0]
                    self.vessel_bvg2s.append([values[0],values[1][0]])
                    vf_upper = self.float_2_rounded_return(values[1][1][1])
                    self.vessel_vf_upper_values[index][self.test_version] = vf_upper
        self.test_version = 1
