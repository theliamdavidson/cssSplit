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

        return group_array, next_array, [""*39], [""*39]#, [""*39]
    def title_creator(self, test_type, iteration):
        return_array=[]
        if test_type == "Food":
            array = [["Pre L Prox Radial","Pre L Prox Ulnar","Pre L distal radial", "Pre L distal Ulnar","Pre  L Prox Pero","Pre L int Pero","Pre  L  Prox PTA", "Pre L Int PTA", "Pre L Distal  Pero", "Pre L Distal PTA"],\
                   ["Post L Prox Radial", "Post L Prox Ulnar", "Post L distal radial", "Post L distal Ulnar", "Post  L Prox Pero", "Post L int Pero", "Post  L Prox PTA", "Post L  Int PTA", "Post L Distal  Pero", "Post  L Distal PTA"]]
        else:
            array = [["R subclavian", "R Brachial", "R Prox Radial", "R prox ulnar", "R Distal radial",	"R Distal Ulnar", "R 1st", "R 2nd", "R 3rd", "R 4th"],\
                     ["L subclavian", "L Brachial", "L Prox Radial", "L prox ulnar", "L Distal radial", "L Distal Ulnar", "L 1st", "L 2nd","L 3rd", "L 4th"], \
                     ["R Prox Pero", "R Inter Pero", "R Low Pero", "R Prox tib", "R inter tib", "R low tib", "R Calc", "R Med arch", "R Lat arch", "R MT cutanesou", "R 1ST", "R 2ND", "R 3RD", "R 4th"],
                     ["L Prox Pero", "L Inter Pero", "L Low Pero", "L Prox tib", "L inter tib", "L low tib", "L Calc", "L Med arch", "L Lat arch", "L MT cutanesou", "L 1ST", "L 2ND", "L 3RD", "L 4th"],
                     ["L EI", "Lower Aorta", "Upper Aorta", "R EI"]
            ]
        for vessels in array[iteration]:
            return_array.append(vessels)
            return_array.append("")
            return_array.append("")
        return return_array, iteration+1
    def raw_file_output(self, test_type): 	
        file_output = []	
        data_storage = self.vessel_primer(test_type)
        list_addr, iteration = self.title_creator(test_type, 0)
        file_output.append(list_addr)
        if test_type == "Food":
            value_looper = self.food_test_values
        else:
            file_output.append([])
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
            list_addr, iteration = self.title_creator(test_type, iteration)
            file_output.append(list_addr)
            for post_vals in self.value_builder(data_storage[1]):
                file_output.append(post_vals)
        else:
            # ue values
            for right_values in self.value_builder(data_storage[0]):
               file_output.append(right_values)
            file_output.pop(-1)
            list_addr, iteration = self.title_creator(test_type, iteration)
            file_output.append(list_addr)
            for left_values in self.value_builder(data_storage[1]):
                file_output.append(left_values)
            # le values
            list_addr, iteration = self.title_creator(test_type, iteration)
            file_output.append(list_addr)
            for right_values in self.value_builder(data_storage[2]):
                file_output.append(right_values)
            file_output[-5].insert(0, "")
            file_output[-4].insert(0, "")
            file_output[-3].insert(0, "")

            list_addr, iteration = self.title_creator(test_type, iteration)
            file_output.append(list_addr)
            for left_values in self.value_builder(data_storage[3]):
                file_output.append(left_values)
            file_output[-5].insert(0, "")
            file_output[-4].insert(0, "")
            file_output[-3].insert(0, "")

            list_addr, iteration = self.title_creator(test_type, iteration)
            file_output.append(list_addr)
            print(file_output)
            for values in self.value_builder(data_storage[4]):
                file_output.append(values)
            for count in range(15):
                file_output[-5].insert(0, "")
                file_output[-4].insert(0, "")
                file_output[-3].insert(0, "")
        return file_output

if __name__ == "__main__":
    print("wrong file loaded; this file is intended to be a helper")