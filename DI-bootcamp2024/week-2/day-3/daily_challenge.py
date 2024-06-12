#challenge-1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
user_word = input("type a word")
word_list = {}
for index, letter in enumerate(user_word):
    if index in word_list:
        word_list[letter].append(index)
    else :
        word_list[letter] = [index]
print(word_list)

#challenge-2
items_purchase = {
  "xilophone": "$40",
  "Honey": "$300",
  "Fan": "$140",
  "Bananas": "$400",
  "zPan": "$10",
  "Spoon": "$20"
}
wallet = "$100" 
convert_wallet = int(wallet.replace("$",""))
items_list = []
for item, price in items_purchase.items():
    convert_value = int(price.replace("$", ""))
    if convert_value < convert_wallet:
        convert_wallet -= convert_value
        items_list.append(item)
if len(items_list) == 0:
    print("nothing")
else:
    items_list.sort()
    print(items_list)