from math import sqrt
from vessel_math_definitions import Vessel_Definition
class Vessel_math(Vessel_Definition):
    def __init__(self):
        super().__init__()

    def float_2_rounded_return(self, digits):
            rounded_digits = round( (float(digits)) *100) / 100
            return (rounded_digits)

    def stand_dev(self, data):
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
                for columns, vessels in enumerate(groups):
                    if vessel_name == vessels:
                        return rows, columns
        print("broke out, failure")
        return -1, -1

    def value_builder(self, sent_values):
        '''
        creates the outputs for a line for line recreation of mark's raw data page.
        send in data one side at a time.
        list -> list
        '''
        group_array = []
        next_array = []
        print("sent values",sent_values)
        for index, vessels in enumerate(sent_values):
            vessels = ['' if val is None else val for val in vessels]
            print("vessels",vessels)
            group_array.append(vessels[0])
            group_array.append(vessels[2])
            next_array.append(vessels[1])
            next_array.append(vessels[3])
            if index <= 9:
                group_array.append("")
                next_array.append("")

        return group_array, next_array, [""*39], [""*39], [""*39]
    
    def raw_file_output(self, test_type): 	
        file_output = [[],[]]	
        data_storage = self.vessel_primer(test_type)
        if test_type == "Food":
            value_looper = self.food_test_values
        else:
            value_looper = self.vessel_values
        
        for results in value_looper:
            print(results)
            rows, columns = self.output_looper(results[0])
            data_storage[rows][columns] = results[1]
        #(data_storage[1]])
        print("data_storage",data_storage)
        if test_type == "Food":
            for pre_vals in self.value_builder(data_storage[0]):
                file_output.append(pre_vals)
            for post_vals in self.value_builder(data_storage[1]):
                file_output.append(post_vals)
        else:
            # ue values
            for right_values in self.value_builder(data_storage[0]):
               file_output.append(right_values)
            file_output.pop(-1)
            for left_values in self.value_builder(data_storage[1]):
                file_output.append(left_values)
            # le values
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