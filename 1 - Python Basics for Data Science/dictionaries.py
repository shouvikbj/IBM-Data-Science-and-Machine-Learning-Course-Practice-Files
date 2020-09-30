d = {
    "key1": "value 1",
    "key2": 10,
    "key3": 20.5,
    "key4": ["Shouvik", 2, 4.3, 'a']
}
print(d)
print(d["key1"])
print(d["key2"])
print(d["key3"])
print(d["key4"])
print(d["key4"][0])
print(d["key4"][1])
print(d["key4"][2])
print(d["key4"][3])
# add element to a dictionary
d.update({"key5": ("Android R", "Android P")})
print(d)
# deleting an element from dictionary
del (d["key2"])
print(d)
# getting list of all the keys
print(d.keys())
# getting list of all the values
print(d.values())