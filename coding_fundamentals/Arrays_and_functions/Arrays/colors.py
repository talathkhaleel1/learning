# - Create a two dimensional list
#   which can contain the different shades of specified colors
# - In `colors[0]` store the shades of green:
#   `"lime", "forest green", "olive", "pale green", "spring green"`
# - In `colors[1]` store the shades of red:
#   `"orange red", "red", "tomato"`
# - In `colors[2]` store the shades of pink:
#   `"orchid", "violet", "pink", "hot pink"`

colors = []
colors0 = ["lime", "forest green", "olive", "pale green", "spring green"]
colors1 = ["orange red", "red", "tomato"]
colors2 = ["orchid", "violet", "pink", "hot pink"]
colors.append(colors0)
colors.append(colors1)
colors.append(colors2)
print(colors)

# colors += colors0, colors1, colors2
# print(colors)

# Sir in my opinion the second solution is a better approach. Please correct me if I am wrong