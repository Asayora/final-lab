from flask import Flask, render_template, request

app = Flask(__name__)
VERSION = "1.0.0"

def calculate(a, b, op):
    if op == "add":
        return a + b
    if op == "sub":
        return a - b
    if op == "mul":
        return a * b
    if op == "div":
        return "Ошибка" if b == 0 else a / b

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        op = request.form["operation"]
        result = calculate(a, b, op)

    return render_template("index.html", result=result, version=VERSION)

if __name__ == "__main__":
    app.run(debug=True)