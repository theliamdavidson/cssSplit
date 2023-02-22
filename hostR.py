from flask import Flask, render_template, request
from food_test import Food_Test
from nvi_test import Nvi_Test
from program_scaffold import Test_Proctor
app = Flask(__name__)

def converter_store(vessel_vals):
    vessel_name = vessel_vals[0]
    vessel_value = vessel_vals[1]
    if patient_instance.test_type == "Food":
        return_val = food.converter(vessel_name, vessel_value)
        food.store_bvg2_value(vessel_name, vessel_value, return_val)
    else:
        return_val = nvi.converter(vessel_name, vessel_value)
        nvi.store_vessel_values(vessel_name, vessel_value, return_val)
def index_call():
    value = patient_instance.value_hunter()

    value_name = patient_instance.vfOpi

    selected_vessel = patient_instance.index_checker()
    
    return render_template("index.html", 
                            selected_vessel = selected_vessel[0],
                            vessels = patient_instance.vessels,
                            name = patient_instance.patient_name, 
                            num = value_name + ": " + value, 
                            test = patient_instance.test_type,
                            current_vessel_values = selected_vessel[1])

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
    print(patient_instance.patient_name)
    return(index_call())
         
@app.route('/index/', methods=['POST','GET'])
def hello():
    patient_instance.patient_name = request.form.get("fname")
    print( request.form.get("fpid"))
    return render_template("index.html",
                            name=patient_instance.patient_name)

@app.route('/update_vessel', methods=['POST','GET'])
def change_current_vessel():  
    if patient_instance.patient_name == "":
        patient_instance.patient_name = request.form.get("fname")
    send_vessels = []
    ingroup = False
    for vessels in patient_instance.vessels:
        ingroup = False
        for finished_vessels in patient_instance.completed_vessel_values:
            if vessels in finished_vessels[0]:
                ingroup = True
        if ingroup == False:
            send_vessels.append(vessels)

    return render_template("vessel.html",
                            name=patient_instance.patient_name,
                            finished_vessel_values=patient_instance.completed_vessel_values,
                            UE_vessels = patient_instance.UE_vessels,
                            LE_vessels = patient_instance.LE_vessels,
                            viscera_vessels = patient_instance.viscera_vessels,
                            skin_vessels = patient_instance.skin_vessels)
                            
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
    print(vessel_i)
    
    for numbs, name in enumerate(patient_instance.vessels):
        if name == vessel_i:
            patient_instance.vessel_name_index = numbs
            break
    print(request.form.get("vessel"))
    
    return(index_call())

@app.route('/confirm_data/', methods=['POST'])
def confirm_data_response():
    response = patient_instance.value_holder(patient_instance.temp_discovered_value_holder) 
    if response is not None:
        converter_store(response)       
    return(index_call())

@app.route('/read_data/', methods=['POST', 'GET'])
def read_data_response():
    return(index_call())

@app.route('/manual_entry', methods=['POST','GET'])
def manual_data():
    #fix this logic before adding it to the user accessable list
    try:
        data_list = [request.form.get("piu"),request.form.get("pil"),request.form.get("vfu"),request.form.get("vfl")]
    except:
        print()
    vessel = patient_instance.temp_discovered_value_holder

    vessel_name = patient_instance.vfOpi
    value =  vessel
    
    selected_vessel = patient_instance.index_checker()
    return render_template("index.html", 
                            selected_vessel = selected_vessel[0],
                            vessels = patient_instance.vessels,
                            name = patient_instance.patient_name, 
                            num = vessel_name + ": " + value,  
                            current_vessel_values = selected_vessel[1])

@app.route('/monophasic_form', methods=['POST', 'GET'])  
def monophasic():
    patient_instance.monophasic_values()
    return(index_call())

@app.route('/view_data', methods=['POST','GET'])
def view_data():
    if patient_instance.patient_name == "":
        patient_instance.patient_name = request.form.get("fname")
    print(patient_instance.completed_vessel_values)
    return render_template("rawdata.html", 
                            name = patient_instance.patient_name, 
                            micro_vessel_results = patient_instance.completed_vessel_values
                            )

@app.route('/results/', methods=['GET','POST'])
def results():
    post_val = []
    if patient_instance.test_type == "NVI":
       nvi.macro_vessel_calculations()
       post_val = nvi.macro_vessel_results
    elif patient_instance.test_type == "Food":
        food.food_test_report()
        post_val = food.food_test_results
    return render_template("results.html", 
                            macro_vessel_values = post_val, 
                            name=patient_instance.patient_name)

@app.route('/print_data/', methods=['GET','POST'])
def print_data():
    patient_instance.PID = request.form.get('fnum')
    print("pid", patient_instance.PID) 
    completed = patient_instance.bvg_2_csv_file()
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
    deletion_attempt = patient_instance.deletion()
    if deletion_attempt == 6:
        return(index_call())
    return(index_call())    #will eventually have a page to undo a deletion
    
if __name__ == '__main__':
    patient_instance = Test_Proctor()
    food = Food_Test()
    nvi = Nvi_Test()
    app.run( debug = True, host='0.0.0.0')