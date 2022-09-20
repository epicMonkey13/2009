#items() method
fruits = {"Watermelon": "pink", "Banana": "white", "cherries": "red"}
x = fruits.items()
fruits["cherries"] = "blue"
fruits["cherries"] = "black"
fruits["Watermelon"] = "blue"
print(x)

#dictionaries don't allow duplicates

#key() methods
fruit = {"Watermelon": "pink", "Banana": "white", "cherries": "red"}
x = fruit.keys()
# fruit["Banana"] = 1800
print(fruit)
# fruit.pop("Banana")
fruit.popitem()
print(x)

xyz = {
    "brand": "maruti suzuki",
    "model": "mustang",
    "year": "1980"
}
xyz.popitem()
print(xyz)
#the last item gets removed

#setdefault() method
abc = {
    "brand": "maruti suzuki",
    "model": "mustang",
    "year": "1980"
}
a = abc.setdefault("model", "bronco")
b = abc.setdefault("color", "red")
print(a)
print(b)
#google

#update() method
abcd = {
    "brand": "maruti suzuki",
    "model": "mustang",
    "year": "1980"
}

print("before update:", abcd)
abcd.update({"color":"white"})
print("after update: ", abcd)
d = abcd.values()
print("only values got updated without any key:", d)




