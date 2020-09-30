t1 = ("disco", 9, 5.3)
print(type(t1))
print(t1[0], t1[1], t1[2])
t2 = ("hard rock", 10)
t3 = t1 + t2
print(t3)
print(t3[0:4])
print(t3[3:5])
t4 = t3
print(t4)
# t3[2] = "dance" ## this is not possible because tuple objects are immutable
t5 = (10, 5, 8, 2, 50)
print(sorted(t5))
# below is the example of nested tuple
t6 = (1, 2, ("pop", "rock"), (3, 4), ("disco", (1, 2)))
print(t6[2], t6[2][0], t6[2][1], t6[3], t6[3][0], t6[3][1], t6[4], t6[4][1],
      t6[4][1][0], t6[4][1][1])
