from math import sqrt
#from file_decoder_for_csv import file_parser
from datetime import datetime
from vessel_math_definitions import Vessel_Definition
from capture_ocr import capture_decoder
class Vessel_math(Vessel_Definition):
    def __init__(self):
        super().__init__()
        #self.file_instance = file_parser()
        self.recent_iterator = 00
        self.vessel_value_holder = ["", [None, None, None, None]]

    def value_holder(self, value_to_store):
        #try:
        type_of_value = value_to_store[0]
        value = value_to_store[1]
        vessel_list = self.vessel_value_holder[1]
        if type_of_value == "PI":
            if vessel_list[0] == None:
                vessel_list[0] = value

            elif vessel_list[1] == None:
                vessel_list[1] = value
                
        elif type_of_value == "VF":
            if vessel_list[2] == None:
                vessel_list[2] = value

            elif vessel_list[3] == None:
                vessel_list[3] = value
        #print(vessel_list)
        self.vessel_value_holder[1] = vessel_list
        return(self.completed_vessel_actions())
            
        #except:
        #    print("vessels",self.vessel_values)
        #    print("index", self.vessel_name_index)
        #    print("error occured, these are the values")

    def completed_vessel_actions(self):
        # in addition to the name, this function checks for completion and returns whether ot os actually complete or just faking
        vessel_list = self.vessel_value_holder[1]
        if None in vessel_list:
                print(vessel_list)
                return("not done")
        self.recent_iterator = 5
        send_list = [self.vessel_value_holder[0]]
        for values in vessel_list:
            send_list.append(values)
        bvg2 = self.converter(send_list)
        self.completed_vessel_values.append(self.vessel_values[self.vessel_name_index])
        self.vessel_value_holder[1]=[None, None, None, None] 
        self.vessel_name_index = self.vessel_name_index + 1
        print(self.vessel_name_index)
        return(bvg2, vessel_list)

    def monophasic_values(self):
        self.vessel_values[self.vessel_name_index][1][1] = 1
        self.vessel_values[self.vessel_name_index][1][3] = .01
        self.recent_iterator = 4
        self.completed_vessel_actions()
    
    def deletion(self):
        vessel_list = self.vessel_values[self.vessel_name_index][1]
        number_iter = self.recent_iterator
        if number_iter < 4:
            vessel_list[number_iter] = None
            number_iter = 6     #six means successful deletion, sets up the way for an undo
        elif number_iter == 4:
            vessel_list[1] = None
            vessel_list[3] = None
            number_iter = 6
        self.vessel_values[self.vessel_name_index][1] = vessel_list
        return(number_iter)

    def value_hunter(self):
        received_value = capture_decoder()
        if received_value[0] == "vessel not found":
            print("nothing found or camera disconnected")
            self.vfOpi = "Value not Found"
            received_value = " "        
        else:
            self.vfOpi = received_value[0]
            if self.vfOpi == "PI":
                print(received_value)
                try:
                    int(received_value[1])
                    if int(received_value[1]) > 999:
                        received_value = received_value[1][:2] + '.' + received_value[1][2:]
                        self.temp_discovered_value_holder = received_value
                    elif int(received_value[1]) > 99:
                        received_value = received_value[1][:1] + '.' + received_value[1][1:]
                        self.temp_discovered_value_holder = received_value
                except ValueError:
                    self.temp_discovered_value_holder = received_value[1]
                    received_value = received_value[1]
            else:
                self.temp_discovered_value_holder = received_value[1]
                received_value = received_value[1]   
        
        return received_value

    def index_checker(self):
        display_vessel = self.vessel_values[self.vessel_name_index][0]
        vessel_return = self.vessel_values[self.vessel_name_index][1]
        return [display_vessel, vessel_return]

    def bvg_2_csv_file(self):
        print(self.file_output)
        print("macro results",self.macro_vessel_results)
        self.neurovascular_index()
        self.file_instance.output_file(self.file_output, self.patient_name, self.PID, datetime.now().strftime("%H-%M_%m-%d-%Y"))
        self.file_instance.csv_creator(self.completed_vessel_values)
        self.file_instance.output_worksheet(self.lssw_file_output)
        print("vessel_values",self.vessel_values)
        print("nvi_values", self.file_output)
        return(True)

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


if __name__ == "__main__":
    print("wrong file loaded; this file is intended to be a helper")