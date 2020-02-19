import web
import app
import json
import csv

render=web.template.render('application/views/')

class Alumnos:
    def GET(self):
        try:
            data=web.input()
            if(data['token']=='1234'):
                action=data['action']
                result={}
                result="matricula,nombre,primer_apellido,segundo_apellido,carrera\n"
                with open('static/csv/alumnos.csv', 'r') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        print(row)
                        result={}
                        result['matricula']=row['matricula']
                        result['nombre']=row['nombre']
                        result['primer_apellido']=row['primer_apellido']
                        result['segundo_apellido']=row['segundo_apellido']
                        result['carrera']=row['carrera']
                return json.dumps(result)
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result