from flask import Flask,request,jsonify,render_template
import datetime
import re

from config import Config
def init_app():
 """Crea y configura la aplicación Flask"""
 
 app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)

 app.config.from_object(Config)
 #Ejercio1
 @app.route('/')
 def hello_world():
  return 'Bienvenidos'
 #return app

#Ejercicio2
 @app.route('/info')
 def info():
  app_name=app.config['APP_NAME']
  return 'bienvenido a la app'
 

#jercicio3

 @app.route('/about')
 def about():
     return {
'app_name':'Routing App',
'description': 'Aplicación para practicar routing en Flask',
'developers': [
{
'nombre': 'Pepe',
'apellido': 'Argento'
},
{
'nombre': 'Maria',
'apellido': 'Fuseneco'
}
],
 'version': '1.0.0'
}
 
 #ejercicio4
 @app.route('/sum/<int:num1>/<int:num2>')
 def suma(num1,num2):
     result= num1 + num2
     return f'la suma de {num1} y {num2} es:{result}'
 
#ejercicio5

#  @app.route('/age_calculator',methods=['GET','POST'])
#  def age_calculator():
#      age= None
#      if request.method=='POST':
#          day = int(request.form.get('day'))
#          month = int(request.form.get('month'))
#          year = int(request.form.get('year'))

#          dob_date = datetime.data(year,month,day)
#          current_date=datetime.datetime.now().date()

#          if dob_date>current_date:
#             age_error='la fecha de nacimiento es posterior a la actual'
         
#          else:
#             age=(current_date - dob_date).day//365
            
#      current_year = datetime.datetime.now().year

#      return render_template('age_calculator.html', age=age,current_year=current_year)



 #ejercicio6
 @app.route('/operate/<string:operation>/<int:num1>/<int:num2>')
 def operate(operation,num1,num2):
     if operation =='sum':
        result = num1 + num2
     elif operation =='sub':
        result=num1-num2
     elif operation =='mult':
        result=num1 * num2
     elif operation =='div':
        if num2 ==0:
            result = num1/num2
        else:
            return jsonify({'error':'la division no esta definida para esos valores'})       
    

     else:
         return jsonify({'error':'la no existe la ruta definida para ese endopoint'})
            
     return jsonify({'result':result})

#ejercicio7

#  @app.route('/operaciones',methods=['GET'])
#  def operaciones():
#      operation= request.args.get('operation')
#      num1=int(request.args.get('num1'))
#      num2=int(request.args.get('num2'))

#      if operation =='sum':
#         result = num1 + num2
#      elif operation =='sub':
#       result=num1-num2
#      elif operation =='mult':
#       result=num1 * num2
#      elif operation =='div':
#        if num2 ==0:
#            result = num1/num2
   
#        else:
#            return jsonify({'error':'la division no esta definida para esos valores'})       
    
#      else:
#          return jsonify({'mensaje':f'operacion no valida:{operation}'})
            
#      return jsonify({'result':result})

#ejercicio8
 @app.route('/title/<string:word>')
 def format_title(word):
     formatted_word=word.capitalize()
     return jsonify({'formatted_word':formatted_word})
 
#ejercicio9
 @app.route('/formatted/<string:dni>')
 def formatted_dni(dni):
     dni_clean = re.sub(r'[.-]','',dni) #remueve puntos y guiones
     if dni_clean.isdigit() and len(dni_clean)==8:
        formatted_dni=int(dni_clean)
        return jsonify({'formatted_dni':formatted_dni})
     else:
        return jsonify({'error':'DNI invalido debe tener 8 caracteres numericos'})
    
    
    
 
 return app
       


 


 
   




