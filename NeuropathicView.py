from flask import Flask, render_template, request
from food_test import Food_Test
from nvi_test import Nvi_Test
from program_scaffold import Test_Proctor
import logging
app = Flask(__name__)

def converter_store(vessel_vals):
    vessel_name = vessel_vals[0]
    vessel_value = vessel_vals[1]
    if patient_instance.test_type == "Food":
        return_val = food.converter(vessel_name, vessel_value)
        patient_instance.food_test_values[patient_instance.vessel_name_index] = vessel_vals
        food.store_bvg2_value(vessel_name, vessel_value, return_val)
    else:
        return_val = nvi.converter(vessel_name, vessel_value)
        patient_instance.vessel_values[patient_instance.vessel_name_index] = vessel_vals
        nvi.store_vessel_values(vessel_name, vessel_value, return_val)   
    patient_instance.completed_vessel_values.append(vessel_vals)
    switcher_val = patient_instance.switcher()
    if switcher_val is not None:
        return switcher_val
    return None

def index_call(end=False):
    if end == False:
        value = patient_instance.value_hunter()
        value_name = patient_instance.vfOpi
        selected_vessel = patient_instance.index_checker()
        logger.debug(nvi.vessel_values)
        logger.debug(patient_instance.vessel_values)
        return render_template("index.html", 
                                selected_vessel = selected_vessel[0],
                                name = patient_instance.patient_name, 
                                num = value_name + ": " + value, 
                                test = patient_instance.test_type,
                                current_vessel_values = selected_vessel[1])
    return render_template("index.html", 
                                selected_vessel =  "None",
                                name = patient_instance.patient_name, 
                                num = "None" + ": " + "None", 
                                test = "Completed",
                                current_vessel_values = "None")
def vessel_setter():
    ue = ["Upper Extremity Pre"]
    le = ["Lower Extremity Pre"]
    viscera = ["Upper Extremity Post"]
    skin = ["Lower Extremity Post"]
    for vessel in food.vessels_for_food_test:
        if vessel in patient_instance.UE_vessels:
            ue.append(vessel)
        elif vessel in patient_instance.LE_vessels:
            le.append(vessel)
        elif vessel[5:] in patient_instance.UE_vessels:
            viscera.append(vessel)
        elif vessel[5:] in patient_instance.LE_vessels:
            skin.append(vessel)
    return(ue,le,viscera,skin)
                 
@app.route('/', methods=['POST','GET'])
def home():
    patient_instance.__init__()
    food.__init__()
    nvi.__init__()
    return render_template('home.html')

@app.route('/home', methods=['POST','GET'])
def althome():
    patient_instance.__init__()
    food.__init__()
    nvi.__init__()
    return render_template('home.html')

@app.route('/landing/', methods=['POST','GET'])
def first_tasks():    
    patient_instance.test_type = request.form.get("test")
    patient_instance.patient_name = request.form.get("fname")
    return(index_call())
         
@app.route('/update_vessel', methods=['POST','GET'])
def change_current_vessel():  
    if patient_instance.test_type == "Food":
        vessel_list = vessel_setter()
    else:
        vessel_list = [patient_instance.UE_vessels, patient_instance.LE_vessels, \
            patient_instance.viscera_vessels, patient_instance.skin_vessels]

    return render_template("vessel.html",
                            name=patient_instance.patient_name,
                            finished_vessel_values=patient_instance.completed_vessel_values,
                            UE_vessels = vessel_list[0],
                            LE_vessels = vessel_list[1],
                            viscera_vessels = vessel_list[2],
                            skin_vessels = vessel_list[3])
                            
@app.route('/confirm_vessel', methods=['POST','GET'])
def confirm_vessel():
    ves_one = request.form.get("uevessel")
    ves_two = request.form.get("levessel")
    ves_three = request.form.get("visvessel")
    ves_four = request.form.get("skinvessel")
    if ves_one is not None:
        vessel_i = ves_one
    elif ves_two is not None:
        vessel_i = ves_two
    elif ves_three is not None:
        vessel_i = ves_three
    elif ves_four is not None:
        vessel_i = ves_four
    if patient_instance.test_type == "Food":
        for numbs, name in enumerate(patient_instance.vessels_for_food_test):
            if name == vessel_i:
                patient_instance.food_test_values[patient_instance.vessel_name_index][1] = patient_instance.vessel_value_holder[1]
                patient_instance.vessel_name_index = numbs
                patient_instance.vessel_value_holder = patient_instance.food_test_values[patient_instance.vessel_name_index]
                return(index_call())
    for numbs, name in enumerate(patient_instance.vessels):
        if name == vessel_i:
            patient_instance.vessel_values[patient_instance.vessel_name_index][1] = patient_instance.vessel_value_holder[1]
            patient_instance.vessel_name_index = numbs
            patient_instance.vessel_value_holder = patient_instance.vessel_values[patient_instance.vessel_name_index]
            break
        
    return(index_call())

@app.route('/confirm_data/', methods=['POST'])
def confirm_data_response():
    response = patient_instance.value_holder() 
    if response is not None:
        done = converter_store(response)    
        if done is not None:
            return(index_call(True))
    return(index_call())

@app.route('/read_data/', methods=['POST', 'GET'])
def read_data_response():
    return(index_call())


@app.route('/monophasic_form', methods=['POST', 'GET'])  
def monophasic():
    response = patient_instance.monophasic_values()
    if response is not None:
        done = converter_store(response)    
        if done is not None:
            return(index_call(True))
    return(index_call())

@app.route('/view_data', methods=['POST','GET'])
def view_data():
    if patient_instance.patient_name == "":
        patient_instance.patient_name = request.form.get("fname")
    return render_template("rawdata.html", 
                            name = patient_instance.patient_name, 
                            micro_vessel_results = patient_instance.completed_vessel_values
                            )

@app.route('/results/', methods=['GET','POST'])
def results():
    post_val = []
    if patient_instance.test_type == "NVI":
       #nvi.macro_vessel_calculations()
       post_val = nvi.macro_vessel_results
    elif patient_instance.test_type == "Food":
        #food.food_test_report() 
        post_val = food.food_test_results
    return render_template("results.html", 
                            macro_vessel_values = post_val, 
                            name=patient_instance.patient_name)

@app.route('/print_data/', methods=['GET','POST'])
def print_data():
    if patient_instance.test_type == "NVI":
        #nvi.neurovascular_index()
        #file_to_print = nvi.file_output
        raw_data = nvi.raw_file_output(patient_instance.test_type)
    else:
        #file_to_print = food.food_test_results
        raw_data = food.raw_file_output(patient_instance.test_type)
    completed = patient_instance.bvg_2_csv_file(raw_data)
    if completed is True:
        success = ""
    else:
        success = "not "
    success += "successful"
    return render_template("print_result.html", 
                            name=patient_instance.patient_name,
                            success=success)

@app.route('/delete_last', methods=['GET','POST'])
def delete_recent():
    
    selected_vessel = patient_instance.index_checker()
    return(render_template("deletion_page.html",
                            selected_vessel = selected_vessel[0],
                            vessels = patient_instance.vessels,
                            current_vessel_values = selected_vessel[1]))    

@app.route('/confirm_delete', methods=['GET','POST'])
def confirm_and_return():
    value_one = request.form.get("piu")
    value_two = request.form.get("pil")
    value_three = request.form.get("vfu")
    value_four = request.form.get("vfl")
    deletion_attempt = patient_instance.deletion([value_one, value_two, value_three, value_four])
    return(index_call())
    

if __name__ == '__main__':
    patient_instance = Test_Proctor()
    food = Food_Test()
    nvi = Nvi_Test()
    logging.basicConfig(filename="debug.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
    logger = logging.getLogger()
    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)
    app.run(host='0.0.0.0', debug = True, use_reloader=False)