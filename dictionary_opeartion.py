# operation - 1 creating Dictionary
my_dict = {"name": "John", "age": 25, "city": "New York"}
# operation - 2 Accessing Value 
print(my_dict["name"])
# operation -3 Adding or Modifying Elements
my_dict["gender"] = "Male"
my_dict["age"] = 26
print(my_dict)
# operation -4 Removing key value pair
del my_dict["city"]
print(my_dict)
popped_value = my_dict.pop("gender")
print(my_dict)
print(f"popped value is {popped_value}")
last_item = my_dict.popitem()
print(my_dict)
print(f"last pop iteam is {last_item}")
# operation -5 Itearting Over a Dictionary
print(my_dict)
for key in my_dict:
    print(key)
for value in my_dict.values():
    print(value)
for key, value in my_dict.items():
    print(key, value)
# opeartion - 6 Checking Dictionary Length
length = len(my_dict)
print(length)
# operation -7 clearing a dictionary
my_dict.clear()
print(my_dict)