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

    def value_builder(self, sent_values):
        '''
        creates the outputs for a line for line recreation of mark's raw data page.
        send in data one side at a time.
        list -> list
        '''
        group_array = []
        next_array = []
        for index, vessels in enumerate(sent_values):
            vessels = ['no' if val is None else val for val in vessels]
            #for value in vessels:
            #    if value is None:
            #        value == ""
            group_array.append(vessels[0])
            group_array.append(vessels[2])
            next_array.append(vessels[1])
            next_array.append(vessels[3])
            print(index,"--------------------------------------------------------")
            if index <= 9:
                group_array.append("")
                next_array.append("")

        return group_array, next_array, [""*39], [""*39], [""*39]
    
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
        #(data_storage[1]])
        for right_values in self.value_builder(data_storage[0]):
            file_output.append(right_values)
        file_output.pop(-1)
        for left_values in self.value_builder(data_storage[1]):
            file_output.append(left_values)
        for right_values in self.value_builder(data_storage[2]):
            file_output.append(right_values)
        file_output[-5].insert(0, "")
        file_output[-4].insert(0, "")
        for left_values in self.value_builder(data_storage[3]):
            file_output.append(left_values)
        file_output[-5].insert(0, "")
        file_output[-4].insert(0, "")
        for values in self.value_builder(data_storage[4]):
            file_output.append(values)
        for count in range(15):
            file_output[-5].insert(0, "")
            file_output[-4].insert(0, "")
        return file_output

if __name__ == "__main__":
    print("wrong file loaded; this file is intended to be a helper")