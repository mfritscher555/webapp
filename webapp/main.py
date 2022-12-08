

from flask import Flask
from flask import render_template, request, redirect
# from logging import FileHandler, WARNING
import math

app = Flask(__name__, template_folder='Templates')

# pi is a global variable since it does not change
pi = 3.141592658979


#
# file_handler = FileHandler('../webapp/webapp/errorlog.txt')
# file_handler.setLevel(WARNING)

@app.route('/', methods=['GET'])
def index():
    area=None
    circumference=None
    radius=None
    return render_template("index.html", area=area, circumference=circumference, radius=radius)


@app.route('/', methods=['GET','POST'])
def indexPost():
    if request.method == "POST":
        radius = request.form['radius']
        # If the input is good:
        try:
            calculatedArea = area(float(radius))
            calculatedCircum = circumference(float(radius))
            return render_template("index.html", area=calculatedArea, circumference=calculatedCircum, radius=radius)
        except ValueError:
            try:
                # If the input contains commas (not necessary when input changed to number)
                radius = radius.replace(",", "")
                calculatedArea = area(float(radius))
                calculatedCircum = circumference(float(radius))
                return render_template("index.html", area=calculatedArea, circumference=calculatedCircum, radius=radius)
            except ValueError: # when the input is empty set these equal to empty as well
                return render_template("index.html", area="", circumference="", radius=radius)
    elif request.method == "GET":
        return redirect('/')


def area(radius):
    value = pi * radius ** 2
    return value



def circumference(radius):
    value = 2 * radius * pi
    return value











if __name__ == "__main__":
    app.debug = True
    app.run(host="127.0.0.1", port=8080, debug=True)