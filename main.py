from food_test import Food_Test
from nvi_test import Nvi_Test
from vessel_math import Vessel_math
from capture_ocr import capture_decoder
import logging

#--------------temp.py below

def vessel_looper(vessel_group):
    index_failure = 0
    return_list = []
    for vessels in vessel_group:
        index_failure += 1
        print(index_failure)
        for index, index_values in enumerate(patient_instance.vessels):
            if index_values == vessels:
                patient_instance.vessel_name_index = index
                break
        patient_instance.vessel_value_holder[0] = vessels
        Not_Complete = True
        while Not_Complete:
            nums_return = capture_decoder()
            #print(nums_return)
            value_holder_return = patient_instance.value_holder(nums_return)
            #print(is_complete)
            if value_holder_return != "not done":
                Not_Complete = False
                return_list.append([vessels, value_holder_return])
    return(return_list)
if __name__ == "__main__":
    logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
    logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
    logger.setLevel(logging.INFO)
    patient_instance = Vessel_math()
    food = Food_Test()
    nvi = Nvi_Test()
    food_vessels = food.vessels_for_food_test
    nvi_vessels = nvi.vessels
    food_values = vessel_looper(food_vessels)
    food.store_bvg2_value(food_values)
    food_values = vessel_looper(food_vessels)
    food.store_bvg2_value(food_values)
    
    logger.info("vessel",food.vessel_bvg2s)
    logger.info("bvg2 values",food.vessel_bvg2_values)
    logger.info("vf",food.vessel_vf_upper_values)
    print("------------------------------------------------------------------------------------------------------------------")
    food.food_test_report()
    nvi_values = vessel_looper(nvi_vessels)
    nvi.store_bvg2_value(nvi_values)
    #print(nvi_values)
    logger.info(nvi.vessel_values)
    logger.info(nvi.group_holder)
    logger.info(nvi.macro_vessel_calculations())
    nvi.neurovascular_index()
    logger.info(nvi.file_output)
    #print(patient_instance.macro_vessel_results)
    #patient_instance.neurovascular_index()
    #print(patient_instance.file_output)
    #patient_instance.bvg_2_csv_file()

    