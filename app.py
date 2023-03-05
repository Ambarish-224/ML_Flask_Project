from flask import Flask


app = Flask(__name__)


@app.route('/')  #localhost: Port_number?home


def home():
    return "This is our first Flask Application"


if __name__ == '__main__':
    app.run(host ='0.0.0.0', port=8000)