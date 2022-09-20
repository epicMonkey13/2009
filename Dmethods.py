#clear()method
car = {
    "brand": "maruti suzuki",
    "model": "mustang",
    "year": "1980"
}
car.clear()
print(car)
#copy method
Name = {
    "brand": "maruti suzuki",
    "model": "mustang",
    "year": "1980"
}
a = Name.copy()
print(a)
#fromkeys method
x = ("apple", "banana", "strawberry")
y = 10
z = dict.fromkeys(x, y)
print(z)

#get() method
xyz = {
    "brand": "maruti suzuki",
    "model": "mustang",
    "year": "1980"
}
b = xyz.get("year")
c = xyz.get("price", "150000")
print(b)
print(c)
#element gets added at the time of get method