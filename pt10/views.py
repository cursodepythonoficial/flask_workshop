from flask.views import MethodView

class MyView(MethodView):
    def dispatch_request(self, *args, **kwargs):
        print("This is called before any request!")
        return super().dispatch_request(*args, **kwargs)

    def get(self):
        return "GET me!"

    def post(self):
        return "POST me!"

    def put(self):
        return "PUT me!"

    def delete(self):
        return "DELETE me!"
