import web

urls = (
    '/', 'Hello',
    '/?', 'application.controllers.alumnos.Alumnos',
)

app = web.application(urls, globals())
class Hello:
    def GET(self):
        return "Hola Yuri\ntoken=1234\nConsultar ?action=get\nBuscar un registro por matricula ?action=search&matricula=xxx\nInsertar un nuevo registro, ?action=put&matricula=xxx&nombre=xxxx&primer_apellido=xxxx&segundo_apellido=xxxx&carrera=xxxx\nBorrar un registro, ?action=delete&matricula=xxxx\nActualizar datos, ?action=update&matricula=xxx&nombre=xxxx&primer_apellido=xxxx&segundo_apellido=xxxx&carrera=xxxx"
if __name__ == "__main__":
    app.run()