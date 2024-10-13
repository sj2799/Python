a = 1          #int
b = 0.7        #float
c = "12"       #string (anything in quotes is considered as string)
d = "Hello"    #string
e = 'Welcome'  #string
f = 6+2j       #complex

print (type(a))
print (type(b))
print (type(c))
print (type(d))
print (type(e))
print (type(f))

list1 = [2, 3.4, [-6, 8], ["apple", 'banana']]  #LIST is ordered, enclosed within square brackets & are mutable

tuple1 = ("lion", ("parrot", "sparrow"), ("cow") ) #TUPLE is ordered, enclosed within parenthesis & are immutable

dict1 = {"name":"emma", "age":20, "canVote": True} #DICT is unordered containing a key:value pair, enclosed within curly brackets
                                                 
print(type(list1))
print(type(tuple1))
print(type(dict1))
print("\n")

#types of type casting:
'''Explicit conversion - Done manually as per requirement. It can be achieved with the help of python's
built-in conversion functions such as int(), float(), hex(), oct(), str(), etc'''

g = "10"
h = 20
print (int(g)+h)

i = 30
j = "20"
k = int(j)
print(i+k)

'''Implicit conversion - Data types in python have different level of ordering (high & low). So, while performing 
any operations on variables with different data types, one of the variable's data type will be changed to higher 
data type (Python converts smaller data type to higher data type to prevent data loss) '''

l = 1.7
m = 9
print(l+m)