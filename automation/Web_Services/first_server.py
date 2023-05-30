from flask import Flask, request # Import class Flask from librabry flask

app = Flask("First Web Server")# Since Flask is a class, instantiate it. Parameter name can be of your choice

@app.route("/")# this is called routing. It is always followed by a function.
# @ is an annotation meaning an additional information about the next line. \
# It adds metadata about the next line.
#  route: tells which http url path, that the function on the next line, will run. It is a way\
# to specify a modified or new url in the application
#  "/" : means the path, such as "https://flask.palletsprojects.com/en/2.0.x/quickstart/". Each "/"
# says the next function or page to be accessed. If nothing is mentioned after the "/" then it is just
# the server page and no path. So it takes the function specified on the line immediately after it.



def first(): #Then we will write a function, function_name can be of your choice
    return "Hello"

# Running an application
# In Git Bash:
# $ export FLASK_APP=file_name(without.py), press enter, then give the run command
# $ flask run
#    You get a warning signal, do not panic
#  * Running on http://127.0.0.1:5000/  , this is the message that will be displayed. This is a
# dedicated IP or the home IP, meaning, IP of this machine itself or Loopback traffic or localhost
#   Check the IP on the browser. 127.0.0.1 will not open.
# In browser you do not have to specify the port number because "https" websites have
# their own default port number, which is 443. To use these we will need some super user privilages
# thus we do not use them.
#   As our website is "http" website we will have to specify the port number :5000 and then you see\
# the webpage load and open with matter as given in the function.

 # Note: print statement are printed on the Git bash and return statements on the webPage.
# Note: Once changes are made in Pycharm, flask run in Git Bash followed by changing parameter values \
#   on the browser page.

# In order to test this always quit the application in Git Bash. Since these are applications which\
# keep running continuously, we need to quit it using ctrl+C and then run the command again by
# giving the command- flask run. refresh the browser page to view changes if any.
#   We can check on the browser localhost_IP- 127.0.0.1:5000/apple , will display "Apple"
#  In other words, each part of the url displays different content on webpage.
# 127.0.0.1:5000 is the server part followed by "/" which is the path. This is then followed by
# the name of the function you would like to execute or display on the webpage

# Here we are trying to run functions using urls
# The above are examples of static variable values given in url. We can also pass \
# parameter variables in url.


# 1)Query Parameters on URL : parameters after the ?

#   Example = 127.0.0.1:5000/apple?num=5&text=pear
# ?  in url means giving a query parameter. Query parameters is a list of key-value pairs. Each
# parameter  is seperated by "&".
# On re-running the flask command in Git bash and refreshing the browser page we see in Git Bash that\
# ImmutableMultiDict <[("num", "5")]> , basicallly details of query parameter has been given therein.
#  Based on these query parameters we can create a website giving conditiona (including if statements)

@app.route("/apple") # this is case-sensitive. the destination path and the following function name
# should be the same.
def apple():
    print("some apples")# request library of flask is used here
    print(request.args) # will give the enitre key:values of the dictionary
    print(request.args["num"])# this is used to check the requests in url. You can also specify the query_name\
    # you intend to check. Since it is a dictionary - ImmutableMultiDict, the query_name would be the
    # key. Just like how you check values for dictionary keys.
    # We can also give multiple paramenter/query_names
    print(request.args["text"])
    lang = (request.args["lang"])
    name =(request.args["hello"])
    if lang == "en":
        return "hello" + name
    elif lang == "it":
        return "Ciao" + name
    return "I don\'t know this language, so I can\'t greet " + name
    # this \ before ' is to say that it is part of string.


# 2)Path Parameters on URL : parameters before the ? in the path of the url itself
@app.route("/help/calculation")
def help_calculation():
    return "if you want to use the calculator go to the /calculation/add link."

@app.route("/calculation/add")
def calculation_add():
    num1 = 5
    num2 = 786
    return str(num1 + num2) # always return a string, int values cannot be returned

@app.route("/calculation/subtract")
def calculation_subtract():
    num1 = 5
    num2 = 791
    return str(num2 - num1) # always return a string, int values cannot be returned

#  rather than duplicating the code, if only the second part, the one after /calculation/"" , can be
# a parameter in its own. This is called path parameter - parameters before the ?

@app.route("/calculation/<operation>") # operation is a parameter which will \
# be passed as a parameter in the below function as well. The operation is mentioned on the browser\
#127.0.0.1:5000/calculation/multipy?num1=5&num2=786
def calculation(operation):
    print(operation)
    num1 = int(request.args["num1"]) # to make values more dynamic we can use values \
    # from query_parameters as well
    num2 = int(request.args["num2"]) # request.args["key_name"], for example: request.args["num1"]
    if operation == "addition":
        return str(num1 + num2)
    if operation == "subtract":
        return str(num2 - num1)
    if operation == "multiply":
        return str(num1 * num2)
    if operation == "divide":
        return str(num2 / num1)
    return "Unsupportive operation"

