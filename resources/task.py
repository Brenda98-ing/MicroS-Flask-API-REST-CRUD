from flask import request, jsonify, Blueprint
from datetime import datetime

from database import tasks


tasks_bp = Blueprint('routes-tasks', __name__)

#DOs funciones pueden tener la misma url -ENDPOINT
#@app.route('/tasks',methods=['POST']) #Que metodo va usar POST - ENVIAR LOS DATOS
@tasks_bp.route('/tasks',methods=['POST'])

def add_task(): #Agregar datos de tabla por parte del cliente
   title= request.json['title']
   created_date=datetime.now().strftime("%x") # 5/22/2021
  
   data=(title,created_date)
   task_id=tasks.insert_task(data)
   
   
   if task_id:
      task=tasks.select_task_by_id(task_id)
      return jsonify({'task':task})
   return jsonify({'message':'Internal Error'})


#NO pueden tener la misma url con el mismo metodo, por eso se cambia
# Si se quiere usar la misma url debe de usarse diferente metodo
#@app.route('/tasks',methods=['GET']) # GET OBTENER LOS DATOS
@tasks_bp.route('/tasks',methods=['GET'])
def get_task():
   data=tasks.select_all_tasks()

   if data:
      return jsonify({'task':data})
   
   elif data == False:
      return jsonify({'message':'Internal Error'})
   else:
      return jsonify({'tasks':{}})



#@app.route('/tasks',methods=['PUT']) # PUT modifica datos
@tasks_bp.route('/tasks',methods=['PUT'])
def update_task(): #Escribir nuestro end-point
   title= request.json['title'] # Estamos tomando el titulo del json |put -es para modificar
   id_arg= request.args.get('id')
    
   if tasks.update_task(id_arg,(title,)): #Si esta modificando correctamente
      task=tasks.select_task_by_id(id_arg)
      return jsonify(task)
   return jsonify({'message':'Internal Error'})

#Vamos a pasar el ide a la misma URL, para que s epueda trabajar con ella, esto se le llama argumentos

#@app.route('/tasks',methods=['DELETE'])
@tasks_bp.route('/tasks',methods=['DELETE'])
def delete_task():
   id_arg=request.args.get('id')

   if tasks.delete_task(id_arg): 
      return jsonify({'message':'TASK DELETED'})
   return jsonify({'message':'Internal Error'})


# COmo ya se uso put - se agrego un parametor al link
#Para esta funcion se va a pasar 2 parametros
# Con la funcion put, primer argumento id y el valor complete
#@app.route('/tasks/completed',methods=['PUT'])
@tasks_bp.route('/tasks/completed',methods=['PUT'])
def complete_task():
   id_arg=request.args.get('id')
   completed=request.args.get('completed')

   if tasks.complete_task(id_arg,completed): 
      return jsonify({'message':'Succesfully'})
   return jsonify({'message':'Internal Error'})

