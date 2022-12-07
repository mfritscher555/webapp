

from flask import Flask
from flask import render_template, request
import math

# pi is a global variable since it does not change
pi = 3.141592658979

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    area=None
    circumference=None
    return render_template("index.html", area=area, circumference=circumference)


@app.route("/", methods=['Post'])
def indexPost():
    radius = request.form['radius']
    calculatedArea = area(radius)
    calulatedCircum = circumference(radius)
    return render_template("index.html", area=calculatedArea, circumference=calulatedCircum)

def area(radius):
    radius = float(radius)
    value = pi * radius ** 2
    return value




def circumference(radius):
    radius = float(radius)
    value = 2 * radius * pi
    return value





if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)