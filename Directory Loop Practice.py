car = {
"brand": "Mazda",
"model": 3.0,
"year": 2006,
"fuel" : "Bensin",
"color": "Grey",
"type": "Hatchback"
}
car1 = {
"brand": "Toyota",
"model": 5.0,
"year": 2020,
"fuel" : "Bensin",
"color": "Black",
"type": "Sedan"
}
car2 = {
"brand": "Harrier",
"model": 3.0,
"year": 2015,
"fuel" : "Bensin",
"color": "Black",
"type": "SUV"
}
print("/////////////////////show segment////////////////////////")
for x in car:
    print(x)
print("/////////////////////show content////////////////////////")
for x in car.values():
    print(x)
print("//////////////////////show all items///////////////////////")
for x in car.items():
    print(x)
print("/////////////////////copy directory////////////////////////")
mycar = car.copy()
print(mycar)
print("/////////////////////more dictionary////////////////////////")
mycars= {
    "Mazda": car,
"Toyota": car1,
"Harrier": car2
}
print(mycars)