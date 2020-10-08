num = 2

# for loop in a range
for i in range(0, num):
    print(i + 1)

for i in range(num):
    print(i + 1)

# for loop in case of tuples
names = ("amrita", "pori", "shouvik", "moni")
for name in names:
    print(name)

# for loop in case of lists
names = ["amrita", "pori", "shouvik", "moni"]
for name in names:
    print(name)

# for loop in case of dictionaries
names = {
    "name_1": "amrita",
    "name_2": "pori",
    "name_3": "shouvik",
    "name_4": "moni"
}
for key, name in names.items():
    print(f"{key} : {name}")