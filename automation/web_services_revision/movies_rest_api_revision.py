from flask import Flask, jsonify, request

app = Flask("movies_api")

movie_id = 0
API_key = "Never give up, strive LEVEL UP"

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



@app.route("/api/movies", methods = ["GET", "POST"])
def get_movies():
    global movies, movie_id, API_key
    if request.method == "GET":
        return jsonify(movies)
    if request.method == "POST":
        if request.args["API_Key"] == API_key: # this is a query parameter as external client will specify based on us sending it to them for verification
            post_movie = request.get_json() # this parses the incoming request in json format
            post_movie["id"] = movie_id
            movie_id += 1
            movies.append(post_movie)
            return jsonify(post_movie)
        else:
            return "error: Invalid API_KEY"


@app.route("/api/movies/<movie_id>", methods = ["GET", "POST"])
def get_movie(movie_id):
    global movies, API_key
    id = int(movie_id)
    for i in range(len(movies)):
        movie_dictionary = movies[i]
        movie = {}
        if movie_dictionary["id"] == id:
            if request.method == "GET":
                movie.update(movies[id - 1])
                return jsonify(movie)



