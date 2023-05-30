from lxml import etree

def read_file(file_name):
    file = open(file_name, "r")
    tree = etree.parse(file_name)#reads data and builds a tree structure of the data
    # The price of all foods (as a list)
    # list of elements or list of strings for which we are in search of data
    # root_element - from which child element - to the final element
    print(tree.xpath("/breakfast_menu/food/price/text()"))# slash denotes from root_element
    # text() --> means give the text value of the data

    # The sum of all the calories
    # XPath way
    print(tree.xpath(sum("/breakfast_menu/food/calories/text()")))
    # python way, this is what is expected
    calories = tree.xpath("/breakfast_menu/food/calories/text()")
    sum_of_calories = 0
    for calorie in calories:
        sum_of_calories += int(calorie)
    print(sum_of_calories)

    # The description of the food with the id: 3
    print(tree.xpath("/breakfast_menu/food[@id = '3']/description/text()"))
    # [@ attribute_name = "value"]

    # The price of "French Toast"
    print(tree.xpath("/breakfast_menu/food/name[text() = 'French toast'/../price/text()"))

    # The concatenated descriptions of all the "savoury" foods
    print(tree.xpath("concat(/breakfast_menu/food[@type = 'savoury']/description/text())"))

    #python way
    description = (tree.xpath("/breakfast_menu/food[@type = 'savoury']/description/text()"))
    concated_descriptions = ""
    for description in description:
        concated_descriptions += description
    print(concated_descriptions)


    # The count of ingredients of the food with id: 2
    #python way
    print(len(tree.xpath("/breakfast_menu/food[@id ='2'/ingredients/ingredient")))
    # XPath way
    print(tree.xpath("count(/breakfast_menu/food[@id ='2'/ingredients/ingredient"))

    # The second ingredient of "Homestyle Breakfast"
    print(tree.xpath("/breakfast_menu/food[@id ='2'/ingredients/ingredient"))