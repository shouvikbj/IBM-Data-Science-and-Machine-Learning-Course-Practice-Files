l = ["Shouvik", 10.1, 1982]
print(l)
# below is a nested list
l2 = ["shouvik", 10.1, 1982, [1, 2], ('A', 1)]
print(l2)
print(l2[0], l2[1], l2[2], l2[3], l2[3][0], l2[3][1], l2[4], l2[4][0],
      l2[4][1])

l2.append(l)
print(l2)

l2.pop(2)
print(l2)

l3 = l2
print(l3[3:5])

l4 = l3 + l
print(l4)

l4.extend(l2)
print(l4)

l4[0] = "Bajpayee"
print(l4)

del (l4[0])
print(l4)

print("Shouvik Bajpayee".split())
print("Shouvik,Bajpayee".split(","))

# below is the example of aliasing
l5 = l4
l5[0] = "Amrita"
print(l5[0])
print(l4[0])

# below is the example of clonel
l6 = l4[:]
l6[0] = "Baaj"
print(l6[0])
print(l4[0])

# help(l) ## gives all available operations that can be performed
## this help() can be used for lists, tuples, dictionary etc.

# the below code clears all the lists
l.clear()
print(l)
l2.clear()
print(l2)
l3.clear()
print(l3)
l4.clear()
print(l4)
l5.clear()
print(l5)
l6.clear()
print(l6)