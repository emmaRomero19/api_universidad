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

if __name__ == "__main__":
    app.run()