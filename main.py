from food_test import Food_Test
from nvi_test import Nvi_Test
from vessel_math import Vessel_math
from capture_ocr import capture_decoder

#--------------temp.py below
    


if __name__ == "__main__":
    patient_instance = Vessel_math()
    food = Food_Test()
    nvi = Nvi_Test()
    for vessels in food.vessels_for_food_test:
        print(vessels)
        patient_instance.vessel_value_holder[0] = vessels
        Not_Complete = True
        while Not_Complete:
            nums_return = capture_decoder()
            #print(nums_return)
            value_holder_return = patient_instance.value_holder(nums_return)
            #print(is_complete)
            if value_holder_return != "not done":
                Not_Complete = False
                food.store_value(vessels, value_holder_return)
            #patient_instance.converter(vessel_array)
    

    print("onto vessel calculations -------------------------------------------")

    #print(patient_instance.macro_vessel_calculations())
    print("------------------------------------------------------------------------------------------------------------------")

    #print(patient_instance.macro_vessel_results)
    #patient_instance.neurovascular_index()
    #print(patient_instance.file_output)
    #patient_instance.bvg_2_csv_file()

    