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