import web

urls = (
    '/(.*)', 'index'
)

app = web.application(urls, globals())


class index:
    def GET(self, name):
        return "Hello " + name + ". How are you today?"


if __name__ == "__main__":
    app.run()
