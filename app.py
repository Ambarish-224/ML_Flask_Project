from flask import Flask


app = Flask(__name__)


@app.route('/', methods = ['GET')  #localhost: Port_number?home


def home():
    return "This is our first Flask Application"


if __name__ == '__main__':
    app.run(debug=True)
