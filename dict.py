#to store data in key and value format
#ordered, changeable, but does not allow duplicates
a = {
    "Technology": "Python",
    "Author": "Guido Van Rossum",
    "year": 1989,
    "year": 2022,
    "year": 2021,
    "stack": ["Java", "Kotlin", "Big Data"],
    "stack": ("Java", "Kotlin", "Big Data")
}
print(a)
print(a["Technology"])
#to check if changeable add another year and it prints the latest entry
print(len(a))
print(type(a))
#can add any data type like above, list and tuple for example

