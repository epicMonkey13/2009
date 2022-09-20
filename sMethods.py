#difference_update google

# set1 = {'a', 'b', 'c'}
# set1.discard('b')
# print(set1)

#intersection
# x = {'Apple', 'MS', 'Delloite'}
# y = {'Wipro', 'Accenture', 'Apple'}
# z = x.intersection_update(y)
# print(z)
#
# x = {'Apple', 'MS', 'Delloite'}
# y = {'Wipro', 'Accenture', 'Apple'}
# f = {'BMW', 'Accenture', 'Apple'}
# z = x.intersection(y)
# z = x.intersection(y)
# x.intersection_update(y)
# print(z)
# print(x)
#
# A = {2, 3, 5, 4}
# B = {2, 5, 100}
# C = {2, 3, 8, 9, 10}
#
# print(B.intersection(A))
# print(B.intersection(C))
# print(A.intersection(C))
#
# print(C.intersection(A, B))
#
# a = {'x', 'o', 'p'}
# b = {'x', 'g', 'h'}
# c = {'x', 's', 'a'}
# d = a.intersection(b,c)
# print(d)

#disjoint
# a = {'a', 'b', 'c', 'd'}
# b = {'e', 'f', 'g', 'h'}
# z = a.isdisjoint(b)
# print(z) #True
#
# a = {'a', 'b', 'c', 'd'}
# b = {'e', 'f', 'g', 'l'}
# o = a.isdisjoint(b)
# print(o)
#google

#subset
# x = {'car', 'toy', 'flight'}
# y = {'a', 'b', 'c', 'car'}
# t = {'a', 'b', 'c', 'car'}
# z = y.issubset(t) #true cos the same, Returns whether another set contains this set or not
# print(z)

# x = {'a', 'b', 'c','car', 'toy', 'flight'}
# x.pop()
# print(x) #removed random item

# x = {'a', 'b', 'c','car', 'toy', 'flight'}
# x.remove('a')
# print(x) #removed specified item

#union Returns a set that contains all items from both sets, duplicates are excluded:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)
print(z)







