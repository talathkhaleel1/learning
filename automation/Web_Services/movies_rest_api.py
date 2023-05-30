from flask import Flask, jsonify, request

app = Flask("json_API")

movie_ID = 0
API_key = "NeverGiveUp"

movies =[{
        "id": 1,
        "title": "Justice League",
        "year": 2017,
        "genre": "Superhero",
        "description": "Justice League premiered in Los Angeles on November 13, 2017, \
        and was released in the United States on November 17, 2017. "},
        {
            "id": 2,
            "title": "Wonder Park",
            "year": 2019,
            "genre": "Adventure comedy",
            "description": "The plot follows a young girl who encounters a real version \
            of her magical amusement park, run by talking animals. "},
        {
            "id": 3,
            "title": "Cars 3",
            "year": 2017,
            "genre": "Animation",
            "description": "In the film, Lightning McQueen sets out to prove to a new generation \
            of high tech race cars that he is still the best racing car in the world. "}
    ]
@app.route("/api/movies",  methods = ["GET", "POST"])

def get_movies():
    global movies, movie_ID, API_key
    if request.method == "GET":
        return jsonify(movies)
    elif request.method == "POST":
        if request.args["API_Key"] == API_key:
            posted_movie = request.get_json() #Parses the incoming JSON request data and returns it.
            posted_movie["id"] = movie_ID
            movie_ID += 1
            movies.append(posted_movie)
            return jsonify(posted_movie)

@app.route("/api/movies/<movie_id>", methods = ["GET", "PUT", "DELETE"])
def get_movie(movie_id):
    global movies, API_key
    id = int(movie_id)
    for i in range(len(movies)):
        if movies[i]["id"] == id:
            if request.method == "GET":
                return jsonify(movies)
            elif request.method == "PUT":
                if request.args["API_KEY"] == API_key:
                    put_movie = request.get_json()
                    put_movie["id"] == id
                    movies[i] = put_movie
            elif request.method == "DELETE":
                if request.args["API_KEY"] == API_key:
                    del movies[i]
                    return "Deleted"
    return "movie with " + movie_id +" not found"

print()

