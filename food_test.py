from food_test_definitions import Food_Test_Definition

class Food_Test(Food_Test_Definition):
    def __init__(self):
        super().__init__()
    def version_checker(self, index):
        if self.vessel_bvg2_values[index][0] != None:
            self.test_version = 1

    def store_bvg2_value(self, vessel_name, vessel_value, bvg2value):
        for index, vessels in enumerate(self.vessels_for_food_test):
            print(self.food_test_values)
            if vessels == vessel_name:
                for point_num, data_point in enumerate(vessel_value):
                    self.food_test_values[index][1][point_num] = self.float_2_rounded_return(data_point)
                if vessel_name[0] == "P":
                    vessel_name = vessel_name[4:]
                    index-=10
                self.version_checker(index)
                self.vessel_bvg2_values[index][self.test_version] = bvg2value
                self.vessel_bvg2s.append([vessel_name, bvg2value])
                vf_upper = self.float_2_rounded_return(vessel_value[1])
                self.vessel_vf_upper_values[index][self.test_version] = vf_upper
                return("done")
        return("not done")
