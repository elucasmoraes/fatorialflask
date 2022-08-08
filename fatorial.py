from math import factorial
from flask import Flask, render_template, request

app = Flask(__name__)
# route -> fatorialdoedinho.com

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    num = request.form.get("numero")
    fat = factorial(int(num))
    return render_template("resultado.html", num = num, fat = fat)

if __name__ == "__main__":
    app.run(debug=True)
