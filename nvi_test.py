from nvi_test_definitions import nvi_test_definitions

class Nvi_Test(nvi_test_definitions):
    def __init__(self):
        super().__init__()

    def store_vessel_values(self, vessel_name, vessel_value, bvg2value):
        for index, vessels in enumerate(self.vessel_values):
            if vessels[0] == vessel_name:
                if vessel_name in self.vessel_exceptions:
                    self.vessel_exception_holder.append([vessel_name,vessel_value[1]])
                for point_num, data_point in enumerate(vessel_value):
                    self.vessel_values[index][1][point_num] = self.float_2_rounded_return(data_point)
                self.bvg_value_placer(vessel_name, bvg2value)
                return("done")
        return("not done")

    def bvg_value_placer(self, vessel_name, vessel_data):
        for group_index, groups in enumerate(self.bvg_groupings):
            if vessel_name in groups:
                sub_group_index = groups.index(vessel_name)
                self.group_holder[group_index][sub_group_index] = vessel_data
                print("found", vessel_name, "in", self.group_holder[group_index])

    
