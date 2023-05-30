from flask import Flask, request, render_template

app = Flask("First server")

@app.route("/")
def first():
    return "Hello"

######### Setting parameters ##########
# 1) Query parameters : Parameter specified in the url after the ? mark. \
# Values for the parameter are specified in the url. It is an ImmutableMultiDictionary


@app.route("/apple")
def apple():
    print("some apples")
    name = request.args["hello"]# recall values just as in dictionary operations
    lang = request.args["lang"]
    if lang == "en":
        return "hello " + name
    if lang == "it":
        return "ciao " + name
    return "I don\'t know this language, so I can\'t greet " + name

# 2) Path parameters : Parameters that are more dynamicand specified before the ? mark in the url.\
# These parameters are part of the url path itself and are functions that associated initiated to run \
# in the background basis some input request from user.

@app.route("/help/calculator")
def help_calculator():
    return "If you want to use the calculator, go to the calculator link."

@app.route("/calc/add")
def calc_add():
    num1 = 45
    num2 = 5
    return str(num1 + num2)

@app.route("/calc/subtract")
def calc_subtract():
    num1 = 54
    num2 = 987
    return str(num2 - num1)


##########  IMPORTANT FOR EXAM ############

#127.0.0.1:5000/calculator/multipy?num1=5&num2=786
@app.route("/calculator/<operation>")# path parameter to be always specifies in the annotation route within "<>"
def calculator(operation):
    print(operation)
    num1 = int(request.args["num1"])# makes using both parameters together. Here we are trying to get values
    num2 = int(request.args["num2"])# for path parameter through query parameter
    if operation == "add":
        return str(num1 + num2)
    if operation == "subtract":
        return str(num1 - num2)
    if operation == "multiply":
        return str(num1 * num2)
    if operation == "divide":
        return str(num1 / num2)
    return "Unsupportive operation"

# there are two ways of sending request:
# 1) we are able to get back HTML
# 2) we are able to get back json

# HTML Templetes
# In the flask documentation you can refer for the same under 'Rendering templates"
# The return statement that we gave intially is what was being displayed on the browser, but we can \
# return the output using render_template(). It is an in-built function.
# render_templete("file_name", name=name). This second parameter is what we will get back now.

@app.route("/blog")
def blog():
    return render_template("blog.html",name = "Fatima", citizen = "Indian", origin = "Makkah",
                           more_details = True, number = 5)
# Parameter1 - the HTML file:
# blog.html has to be an existing file. So here we shall create a blog.html file. \
# All HTML files should be put in a templates folder. So we need to create a new folder called\
# "templates". we can say that these templates serve the HTML files.

# Parameter2 - is a special parameter. It is from here that one can give parameters to the HTML file
# for the purpose of temeplating. Temepelating is using % within which you can actually pass a \
# Python code to generate a HTML file that it can serve.
# refer line 10 of the HTML file. we have stated {{name}}. "{{ }}", we pass parameters within this curly \
# brackets. we have written {{name}} because our variable on this page, line 76, to pass parameter is\
# "name". So in the HTML file, the value given in this file for this variable will be substituted \
# on the browser . It is not just a word but we can add multiple stuff there. We can pass multiple \
# parameters for render_template(). Not just this, we can write codes within this, as in pass\
# "if statements' and "for loops" as well. These control structures have to be written within "{% %}".
# these codes have to be explicitly closed by specifying {% endif %} after the lines for which the \
# code is written.
#  Basically, the render_tempelate() will not only substitue values in HTML file but also read the \
#  code and executes the code. Basis the information and conditions given , it will alter the display \
#  of information on the browser. If we do not specify parameter values in this file, then a string\
# value is taken as an empty string, a number as 0 and a boolean as False.
#  We can also include a "for loop"