import web

urls = (
    '/', 'Hello',
    '/alumnos/?', 'application.controllers.alumnos.Alumnos',
)

app = web.application(urls, globals())
class Hello:
    def GET(self):
        return "Hola Yuri\ntoken=1234\nConsultar /alumnos/?action=get\nBuscar un registro por matricula /alumnos/?action=search&matricula=xxx\nInsertar un nuevo registro, /alumnos/?action=put&matricula=xxx&nombre=xxxx&primer_apellido=xxxx&segundo_apellido=xxxx&carrera=xxxx\nBorrar un registro, /alumnos/?action=delete&matricula=xxxx\nActualizar datos, /alumnos/?action=update&matricula=xxx&nombre=xxxx&primer_apellido=xxxx&segundo_apellido=xxxx&carrera=xxxx"
if __name__ == "__main__":
    app.run()