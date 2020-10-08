a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
# a = 6
# b = 7
if (a == b):
    print("a == b")
elif (a < b):
    print("a < b")
else:
    print("a > b")

c = input("Enter a string: ")
d = input("Enter another string: ")
# c = "shouvik"
# d = "bajpayee"
if (c == d):
    print("same strings.")
else:
    print("different strings.")

e = int(input("Enter a number: "))
# e = 2
i = 0
# while loop
while i < e:
    print(f"Hi {i+1}")
    i += 1

# for loop
for i in range(0, e):
    print(f"Hi {i+1}")

# logical and operation
f = True
g = False
if (f and g):
    print("both are true")
else:
    print("one of them or both are flase")

if (f or g):
    print("one of them or both are true")
else:
    print("both are false")