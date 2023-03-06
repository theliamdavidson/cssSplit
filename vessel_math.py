from math import sqrt
from vessel_math_definitions import Vessel_Definition
class Vessel_math(Vessel_Definition):
    def __init__(self):
        super().__init__()
        #self.file_instance = file_parser()

    def float_2_rounded_return(self, digits):
            rounded_digits = round( (float(digits)) *100) / 100
            return (rounded_digits)

    def stand_dev(self, data):
        print("in standard dev", data)
        sampSize = len(data)
        sum = 0.0
        standardDeviation = 0.0
        for i in range(sampSize):
            data[i] = float(data[i])
            sum += data[i]
        mean = sum/sampSize
        for i in range(sampSize):
            standardDeviation += pow(data[i] - mean, 2)
        return sqrt(standardDeviation/sampSize) 

    def output_looper(self, vessel_name):
        for rows, groups in enumerate(self.vessel_rows):
                print(groups)
                print(vessel_name)
                for columns, vessels in enumerate(groups):
                    if vessel_name == vessels:
                        return rows, columns
                    
    def ue_builder(self, right_left_values):
        return_array = []
        print("left-right",right_left_values)
        for sides in right_left_values:
            print("sides",sides)
            group_array = []
            next_array = []
            for vessels in sides:
                for value in vessels:
                    if value is None:
                        value == ""
                print("vessels",vessels)
                group_array.append(vessels[0])
                group_array.append(vessels[2])
                group_array.append("")
                next_array.append(vessels[1])
                next_array.append(vessels[3])
                next_array.append("")
            while len(group_array) <= 39:
                group_array.append("")
            # being explicit on the off chance a bug 
            # causes the lists to be different sizes    
            while len(next_array) <= 39:
                next_array.append("")
            return_array.append([group_array])
            return_array.append([next_array])
            return_array.append([""*39])
            return_array.append([""*39])  

        return_array.append([""*39])
        print("return",return_array)
        return return_array

    def le_builder(self, right_left_values):
        return_array = []
        for sides in right_left_values:
            group_array = [""]
            next_array = [""]
            counter = 0
            for vessels in sides:
                group_array.append(vessels[0])
                group_array.append(vessels[2])
                next_array.append(vessels[1])
                next_array.append(vessels[3])
                if counter >= 9:
                    group_array.append("")
                    next_array.append("")
                counter += 1
            while len(group_array) <= 39:
                group_array.append("")
            # being explicit on the off chance a bug 
            # causes the lists to be different sizes    
            while len(next_array) <= 39:
                next_array.append("")
            return_array.append([group_array])
            return_array.append([next_array])
            return_array.append([""*39])
            return_array.append([""*39]) 
            return_array.append([""*39])   

        return return_array
    def torso(self, values):
        return_array = [""*15]
        group_array = []
        next_array = []
        for vessels in values:
            group_array.append(vessels[0])
            group_array.append(vessels[2])
            group_array.append("")
            next_array.append(vessels[1])
            next_array.append(vessels[3])
            next_array.append("")
        while len(group_array) <= 39:
            group_array.append("")
        # being explicit on the off chance a bug 
        # causes the lists to be different sizes    
        while len(next_array) <= 39:
            next_array.append("")
        return_array.append(group_array)
        return_array.append(next_array)  
        return return_array
    
    def raw_file_output(self): 	
        data_storage = [
                        [
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None]  
                        ],       \
                        
                        [
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None]
                        ],       \
                        
                        [
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None] 
                        ],                                     \
                        
                        [
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None]
                        ],                                      \
                        
                        [
                        [None, None, None, None], [None, None, None, None], \
                        [None, None, None, None], [None, None, None, None]
                        ]                                            \
                    ]  
        file_output = [[],[]]	
        for results in self.vessel_values:
            rows, columns = self.output_looper(results[0])
            data_storage[rows][columns] = results[1]
            print(rows, columns, data_storage[rows][columns])
        print(data_storage)
        print("----------------------------------------")
        file_output.append(self.ue_builder([data_storage[0], data_storage[1]]))
        file_output.append(self.le_builder([data_storage[2], data_storage[3]]))
        file_output.append(self.torso(data_storage[4]))
        return file_output

if __name__ == "__main__":
    print("wrong file loaded; this file is intended to be a helper")