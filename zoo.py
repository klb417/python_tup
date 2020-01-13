zoo = ("dog", "cat", "lizard", "frog", "cow",
       "salmon", "elephant", "bat", "bird", "dragon")

print(zoo.index("lizard"))


animal_to_find = "salmon"
if animal_to_find in zoo:
    print(f"{animal_to_find} was found")

(animal_01, animal_02, animal_03, animal_04, animal_05,
 animal_06, animal_07, animal_08, animal_09, animal_10) = zoo

print(animal_01)
print(animal_02)
print(animal_03)
print(animal_04)
print(animal_05)
print(animal_06)
print(animal_07)
print(animal_08)
print(animal_09)
print(animal_10)

zooList = list(zoo)
zooList.extend(["gopher", "rabbit", "deer"])

zoo = tuple(zooList)

print(zoo)
