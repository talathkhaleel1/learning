from flask import Flask, jsonify, request

app = Flask("my-JSON-api")

# Here we will learn to retrive any json format of the data, which is in the form of lists\
# and dictionaries
# use Flask documentation for referencing.
# export FLASK_APP=file_name (without .py) --> indicates the file which has to be run
# flask run --> runs the code in the file mentioned in export FLASK_APP

# we can view this on 127.0.0.1:5000
@app.route("/", methods = ["GET", "POST"])
def main():
    print(request.method)
    my_foods = [
        {"name" : "apple", "type":"fruit"},
        {"name": "cucumber", "type": "vegetable"}
    ]
    return jsonify(my_foods)
# to return any data in json format, there is a special function called "jsonify" \
# which has to be imported. We need to use it in return statement. It is basically a built-in function
# and you need to put inside this function what you would like to return/ display. It can take\
# multiple inputs. It will convert data into a string but in json format. In simple words, we can \
# return various data structures as well. It works with lists and dictionaries.

########## Lets really try writing an API ###############
# To really test an API we will need a special software called ""POSTMAN" to test it. You can find\
#the same on "postman.com". It is a tool for sending test http requests. So far we learnt to \
# send http requests using Python code. In Postman, we will do the same using this application \
# and not with code.

##### Steps to use POSTMAN #######
# 1) www.postman.com
# 2) sign in
# 3) After signing in we can actually download and run the application.\
#   You can wrok online on it without having to download. If you want to download, then \
#   -> Download destop app -> Download the app -> install it -> sign in, in the desktop application \
#   -> workspaces -> create new workspace -> name it the way you want -> Create workspace \
#   -> to send http request click on " + " button and then good to send an http request.
# 4) If you intend to do it online follow these steps: \
#   -> Workspaces -> My workspace -> click on " + " button -> specify the url (for example, \
#   127.0.0.1:5000/ as value for GET ( we are working on GET request. This can be changed \
#   using the drop-down on the application page. Otherwise by default it will be a GET request) \
#   -> click SEND. You will see the data you had specified.

# POSTMAN is also good for testing any other API, we checked with giphy. it works but my localhost\
#  does not work. However, it is a better tool to check APIs as it displays data in amore neater \
#  and organised form.

### NOTE: The top bar of the browser takes only GET requests. If you intend to check POST, PUT, \
# PATCH, DELETE or any other form of request, it is always better to check with POSTMAN.

#### Handling a POST Request ###########
# by default @app.route("/") works only with GET request.
# check flask documentation or google flask handle post request.
# in the route we need to specify the request method. -> @app.route("/path", method = "GET", "POST")
# flask run on Git Bash
# But we need to differentiate between get and post request because it is the same data which \
# is being displayed. How do we do it? We need to import request. There is a property of this \
# request, request.method to be specified in the function and in the git Bash it will display\
# which method is being applied

##########  Lets Create an API for storing books############
# We will need multiple APIs - to store books, get books and their data, add new books


books = [{"name": "Harry Porter", "author": "J K Rowling"},
         {"name": "Harry Porter1", "author": "J K Rowling"},
         {"name": "Harry Porter2", "author": "J K Rowling"}]
last_book_id = 0 # as we need to give some unique value for the identification of a specific book
@app.route("/api/books", methods = ["GET", "POST", "DELETE"])
# if it is GET request json should list all of the books
# if it is a POST request, should create a new book and to the list of books
# if it is  a DELETE request it should delete the last book.
def api_books():
    global books, last_book_id # to use variables outside the function we need to declare them so we use the word global
#     first we should be able to send a GET request and get a list of all the books
    if request.method == "GET":
        return jsonify(books)
#     adding a new book : in the body of the http request. In POSTMAN -> body -> JSON \
#     -> write the content you wish to display
    if request.method == "POST":# here we need to save data to create a new object and append it to\
        # the list of books. We can google using flask read post data json
        book = request.get_json()# data has been given in POSTMAN and the same data is retrived \
        book["id"] = last_book_id # and saved into this variable and now we add an ID key to the dictionary
        last_book_id += 1 # we inceament the book id to assign the id to new book
        books.append(book)# we will add this book to the list of books
        return jsonify(book)# thsi is what will be viewed y the client
#  everytime we send a post request on post man with new data in the body and check \
#  with get request then we can view the list of books saved in the books variable.


 ######## listing a book by its ID #####
@app.route("/api/books/<book_id>")# path parameter, in url we need to specify the route/ path correctly, \
# name of def could be something different
def single_book_endpoint(book_id):
    global books
    for book in books:
        if book["id"] == int(book_id):
            return jsonify(book)
# sending a 404 error if item is not found. Check flask send response code.
    return "Book not found," ,404


