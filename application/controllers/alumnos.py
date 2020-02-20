import web
import app
import json
import csv

render=web.template.render('application/views/')

class Alumnos:
    def GET(self):
        try:
            data=web.input()
            if(data['action']=='get' and data['token']=='1234'):
                inf={}
                inf['version']="0.01"
                inf['status']="200 ok"
                result="matricula,nombre,primer_apellido,segundo_apellido,carrera\n"
                with open('static/csv/alumnos.csv', 'r') as csvfile:
                    reader = csv.DictReader(csvfile)
                    result=[]
                    for row in reader:
                        resulta={}
                        resulta['matricula']=row['matricula']
                        resulta['nombre']=row['nombre']
                        resulta['primer_apellido']=row['primer_apellido']
                        resulta['segundo_apellido']=row['segundo_apellido']
                        resulta['carrera']=row['carrera']
                        result.append(resulta)
                    inf['alumno']=result
                    return json.dumps(inf)
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result