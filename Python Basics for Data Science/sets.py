# sets doesn't contain duplicate elements and doesn't record insertion order
s = {"piku", 10, 3.5, 10, "piku", 3.5}
print(s)
# typecasting a list to a set
l = ["phone", "android", "phone", "android", "apple"]
s2 = set(l)
print(l)
print(s2)
#set operations
s3 = {"thriller", "men in black", "ac/dc"}
print(s3)
s3.add("iron man")
print(s3)
s3.remove("ac/dc")
print(s3)
## checking item appearance in a set
print("iron man" in s3)  # prints True
print("ac/dc" in s3)  # prints False
## mathematical set operations
s4 = {"captain america", "thor", "iron man"}
### checking intersection of two sets
print(s3 & s4)  # prints "iron man" as it is the only common element
print(s3.intersection(s4))  # does the same thing as above
### union of two sets
s5 = s3.union(s4)
print(s5)
### checking subset
print(s4.issubset(s5))  # prints True
print(s3.issubset(s4))  # prints Flase
