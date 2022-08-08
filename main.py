from flask import Flask, render_template, request
from src.calc import bmi, bmi_status

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html', height="", weight="", bmi="", status="")

@app.route("/", methods=['GET', 'POST'])
def calc():
    if request.method == "POST":
        height = request.form["height"]
        weight = request.form["weight"]
        user_bmi = bmi(float(height), float(weight))
        status = bmi_status(user_bmi)
        return render_template('home.html', height=height, weight=weight, bmi=user_bmi, status=status)
    else:
        return render_template('home.html', height="", weight="", bmi="", status="")


if __name__ == '__main__':
   app.run()
