# Add "My todo:" to the beginning of the todoText
# Add " - Download games" to the end of the todoText
# Add " - Diablo" to the end of the todoText but with indention

# Expected output:

# My todo:
#  - Buy milk
#  - Download games
#      - Diablo

# todoText = " - Buy milk\n"
#
# print(todoText)

todoText = " - Buy milk\n"
edit_todoText = todoText.find(' " ' )
todoText = "My todo:\n" + todoText[::] + " - Download games\n" + "    - Diablo"
print(todoText)