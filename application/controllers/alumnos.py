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
                if(data['action']=="get"):
                    inf={}
                    inf['version']="0.01"
                    inf['status']="200 ok"  
                    result="matricula,nombre,primer_apellido,segundo_apellido,carrera\n"
                    with open('static/csv/alumnos.csv', 'r') as csvfile:
                        reader = csv.DictReader(csvfile)
                        result=[]
                        for row in reader:
                            resulta={}
                            resulta['matricula']=str(row['matricula'])
                            resulta['nombre']=str(row['nombre'])
                            resulta['primer_apellido']=str(row['primer_apellido'])
                            resulta['segundo_apellido']=str(row['segundo_apellido'])
                            resulta['carrera']=str(row['carrera'])
                            result.append(resulta)
                        inf['alumno']=result
                        return json.dumps(inf)

                if(data['action']=="insert"):
                    inf={}
                    inf['version']="0.01"
                    inf['status']="200 ok"  
                    matricula=str(data['matricula'])
                    nombre=str(data['nombre'])
                    primer_apellido=str(data['primer_apellido'])
                    segundo_apellido=str(data['segundo_apellido'])
                    carrera=str(data['carrera'])
                    res=[]
                    res.append(matricula)
                    res.append(nombre)
                    res.append(primer_apellido)
                    res.append(segundo_apellido)
                    res.append(carrera)
                    resulta={}
                    resulta['matricula']=matricula
                    resulta['nombre']=nombre
                    resulta['primer_apellido']=primer_apellido
                    resulta['segundo_apellido']=segundo_apellido
                    resulta['carrera']=carrera
                    result=[]
                    result.append(resulta)
                    inf['alumno']=result
                    
                    with open('static/csv/alumnos.csv','a+', newline='') as variable_cualquiera:
                        writer=csv.writer(variable_cualquiera)
                        writer.writerow(res)
                    return json.dumps(inf)
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result