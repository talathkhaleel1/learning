

def read_file_and_get_ratings_and_authors(file_path):
    try:
        file = open(file_path, 'r')
        content = file.readlines()
        ratings = []
        authors = []
        for row_index in range(1, len(content)):
            data = content[row_index].split(",")
            ratings.append(data[-2])
            authors.append(data[-1])
        file.close()
        ratings_and_authors = dict(zip(ratings, authors))
    except:
        print('Unable to read file: ' + file_path)
    finally:
        return ratings_and_authors

def convert_rating_to_float(rating_and_authors):
    key_values = rating_and_authors.items()
    float_rating_and_str_authors= {float(k) : (v) for k, v in key_values }
    return float_rating_and_str_authors

def get_five_highest_ratings(float_rating__and_authors):
    ratings = float_rating__and_authors.keys()
    sorted_ratings = sorted(ratings)
    top_five_ratings = (sorted_ratings[-5::])
    top_five_ratings_ascending_order = top_five_ratings[::-1]
    return top_five_ratings_ascending_order

def list_of_five_highest_rated_authors(float_ratings_and_authors,highest_five_ratings):
    authors = []
    for i in highest_five_ratings:
        for k,v in float_ratings_and_authors.items():
            if k == i:
                authors.append(v)
    return authors

def write_author_file(five_highest_rated_authors):
    author_file = open("highest_rated_authors.csv", "w")
    author_file.writelines(five_highest_rated_authors)
    author_file.close()
    return author_file



def highest_rated_authors(file_name):
    rating_and_authors = read_file_and_get_ratings_and_authors(file_name)
    float_rating__and_authors = convert_rating_to_float(rating_and_authors)
    highest_five_ratings = get_five_highest_ratings(float_rating__and_authors)
    five_highest_rated_authors = list_of_five_highest_rated_authors(float_rating__and_authors, highest_five_ratings)
    highest_rated_authors = write_author_file(five_highest_rated_authors)
    return highest_rated_authors

print(highest_rated_authors("details_of_books.csv"))