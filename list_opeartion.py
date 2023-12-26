# operation - 1 creating a list
name = ["Parth Jadhao","Swaraj Sakhare","Soham","Indrajet"]
# operation - 2 Accessing
# Accessing elements in list by Positive Index
print("----------------positive Indexing----------------")
print(name[0])
print(name[1])
print(name[2])
print(name[3])
# Accessing elements in list by Negative Index
print("----------------negative Indexing----------------")
print(name[-4])
print(name[-3])
print(name[-2])
print(name[-1])
# operation - 3 Slicing
print("----------------performing slicing operations----------------")
subName = name[0:2]
print(subName)
# operation - 4 Appending and Extending
# Appending
print("---------------performing appending and extending operations---------------")
name.append("Pratham")
print(name)
# Extending
name.extend(["Piyush","Aditya","Neel","Advait"])
print(name)
# operation -5 Inserting operations
print("---------------performing Insertion operatation at specific position---------------")
name.insert(0,"Siya Jadhao")
print(name)
# operation - 6 Removing operations
print("---------------performing Removing Operation---------------")
# Removing by value
name.remove("Parth Jadhao")
print(name)
# Removing by index
del name[2]
# pop an element by index
popped_value = name.pop(0)
print(f"popped element is {popped_value}")
print(name)
# operation -7 Finding Elements
print("---------------Finding Elements---------------")
print("Swaraj Sakhare" in name) 
print(name.index("Pratham"))
# operation - 8 Sorting
number = [45,23,56,12,65,34,23,87]
print(number)
number.sort()
print(number)
number.sort(reverse=True)
print(number)
# operation - 9 Length
print(len(number))