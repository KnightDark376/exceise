# def double(x):
#     return x * 2
# def add(x, y):
#     return x + y
# def product(x, y, z):
#     return x * y * z

double = lambda x : x * 2
add = lambda x, y: x + y
product = lambda x, y, z: x * y * z

print(double(10))
print(add(10,20))
print(product(10, 20, 30))

#filter, reduce and map
my_list = [2, 5, 8, 10, 9, 3]
my_list2 = [2, 4, 7, 5, 9, 10]
a = map(lambda x: x * 2, my_list)
print(list(a))
b = map(lambda x, y: x + y, my_list, my_list2)
print(list(b))

c = filter(lambda x: x%2==0, my_list)
print(list(c))

d = filter(lambda x: True if x > 5 else False, my_list)
print(list(d))

e = reduce(lambda x , y : x +  y, my_list)
print(e)
