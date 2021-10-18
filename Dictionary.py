car = {
"brand": "Mazda",
"model": 3.0,
"year": 2006,
"fuel" : "Bensin",
"color": "Grey",
"type": "Hatchback"
}
print(car) #show overall situation inside the directory

print("////////////////////// ////////////////////////////////////")
x = car.values()
print(x) #show contents only
print("//////////////////////change items inside the directory ////////////////////////////////////")
car["color"] = "Blue"
car["year"] = 2006
print(car)

print("//////////////////////add new items in directory ////////////////////////////////////")

car.update({"Transmission": "Manual"})
print(car)
print("////////////// Removing items from directory//////////////")
del car["type"]
print(car)







