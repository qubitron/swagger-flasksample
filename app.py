import flask
from flasgger import Swagger

app = flask.Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def get_index():
    """
    Index API, returns "Hello!"
    ---
    responses:
      200:
        description: the word "Hello!"
    """
    return "Hello!"

@app.route('/number/<number>')
def get_number(number):
    """
    Repeats back a number to you
    ---
    parameters:
      - name: number
        in: path
        type: string
        description: the number
    responses:
        200:
            description: Hello number!
    """

    return "Hello {}!".format(number)

app.run(debug=True)
