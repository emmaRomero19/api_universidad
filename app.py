import web

urls = (
    '/', 'Hello',
    '/static', 'Hello',
    '/alumnos/?', 'application.controllers.alumnos.Alumnos',
)
app = web.application(urls, globals())
class Hello:
    def GET(self):
        return "Hola Yuri"
class Error:
    def GET(self):
        return "UPSI"


if __name__ == "__main__":
    app.run()