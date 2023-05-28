# Post-it
# Create a PostIt class that has
# a background_color
# a text on it
# a text_color
# Create a few example post-it objects:
# an orange with blue text: "Idea 1"
# a pink with black text: "Awesome"
# a yellow with green text: "Superb!"


# post_it={'name':'my_post_it',
#          'post_it_number': 1,
#          'background':...,
#          'text_on_it':...,
#          'text_color':...}
# my_post_it = post_it(name ,post_it_number)
# my_post_it.background(mention_color)
# my_post_it.text_on_it(what_text_you_want_to_write)
# my_post_it.text_color(mention_text_color)

# class Post_it(object):
#     #constructor - function responsible for the construction of the function.
#     def __init__(self, name, post_it_number, background, text_on_it, text_color):
#         self.name = name
#         self.post_it_number = post_it_number
#         self.background = background
#         self.text_on_it = text_on_it
#         self.text_color = text_color
        #return command for this function not necessary as this function is called by default.


    # def background(color):
    #     if background == Orange:
    #
    #         return "Idea 1"
    #
    #
    # def text_on_it(text):
    #     pass
    #
    # def text_color(text_color):
    #     pass


class Post_It:

    def __init__(self, background_color, text, text_color):
        self.background = background_color
        self.text = text
        self.text_color = text_color

    def __str__(self):
        return self.text