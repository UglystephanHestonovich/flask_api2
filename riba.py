from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    a = request.json.values()
    b = sum(a)
    c = {'sum': b}
    return c

app.run()