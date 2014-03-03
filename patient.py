from bottle import run, get, post, request, delete, put
patient_info={}
 
@post('/patient/create')
def create():
    patient_id = request.POST['id']
    patient_name = request.POST['name']
    patient_gender = request.POST['gender']
    patient_age = request.POST['age']
    patient_address = request.POST['address']
    patient_phone = request.POST['phone']
    store_info={}
    store_info.update({"Name":patient_name})
    store_info.update({"Gender":patient_gender})
    store_info.update({"Age":patient_age})
    store_info.update({"Address":patient_address})
    store_info.update({"Phone":patient_phone})
    
    patient_info.update({patient_id:store_info})
    return patient_info

@get('/patient/show/<patient_id>')
def show(patient_id):
    if patient_id not in patient_info.keys():
        return 'This is not a correct patient id'
    else:
        return patient_info[patient_id]

@put('/patient/update/<patient_id>')
def update(patient_id):
    patient_name = request.POST['name']
    patient_gender = request.POST['gender']
    patient_age = request.POST['age']
    patient_address = request.POST['adpatientdress']
    patient_phone = request.POST['phone']
    store_info={}
    store_info.update({"Name":patient_name})
    store_info.update({"Gender":patient_gender})
    store_info.update({"Age":patient_age})
    store_info.update({"Address":patient_address})
    store_info.update({"Phone":patient_phone})
    patient_info.update({patient_id:store_info})
    return patient_info
   


@delete('/patient/delete/<patient_id>')
def delete(patient_id):
    patient_info.pop(patient_id)
    return patient_info


run(host='localhost',port=8080)
