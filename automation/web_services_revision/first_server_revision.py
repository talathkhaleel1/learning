from flask import Flask, request, render_template

app = Flask("web server")

@app.route("/")
def first():
    return "I want to score maximum marks in all subjects"

#Query parameters : http://127.0.0.1:5000/fruits?lang=hu&fruit=alma

@app.route("/fruits")
def get_fruits():
    print("fruits")
    lang = request.args["lang"]
    fruit = request.args["fruit"]
    if lang == "en":
        return "fruit is " + fruit
    if lang == "in":
        return "fruit is " + fruit
    if lang == "hu":
        return "fruit is " + fruit
    return "I don\'t know this language."

#Path parameters
@app.route("/calculation/<operation>")#path parameter
def calculation(operation):
    print(operation)
    num1 = int(request.args["num1"])# query parameter
    num2 = int(request.args["num2"])
    if operation == "addition":
        return str(num1 + num2)
    if operation == "subtraction":
        return str(num1 - num2)
    if operation == "multiplication":
        return str(num1 * num2)
    if operation == "division":
        return str(num1 / num2)
    return "Unsupportive operation"

@app.route("/render/html")# the folder created should always be names as "templates"
def render_html():
    return render_template("first_server.html", name = "Fatima", more_details = True,\
                           citizen = "Indian", age = 36)


