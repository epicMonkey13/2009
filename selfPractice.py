# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.popitem()
#
# print(x)
# #The removed item is the return value of the pop() method
#
# x = ('key1', 'key2', 'key3')
# y = 0
#
# thisdict = dict.fromkeys(x, y)
#
#
# print(thisdict)
#
#
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.items()
# print(x)
#
#
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# g = car.items()
# car["year"] = 2018
# print(g)


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# k = car.setdefault("color", "red")
# print(k)
#Get the value of the "model" item:


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.values()
# print(x)
#keys don't get only values

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.values()
#
# car["year"] = 2018
#
# print(x)
#When a values is changed in the dictionary, the view object also gets updated

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
#
# res = dict.fromkeys(employees, defaults)
# print(res)
#
# # Individual data
# print(res["Kelly"])

#The fromkeys() method returns a dictionary with the specified keys and the specified value.

# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york" }
#
# keys = ["name", "salary"]
#
# newDict = {k: sampleDict[k] for k in keys}
# print(newDict)

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
#
# # keys to extract
# keys = ["name", "salary"]


#
# # new dict
# res = dict()
#
# for k in keys:
#     # add current key with its va;ue from sample_dict
#     res.update({k: sample_dict[k]})
# print(res)

#Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)
