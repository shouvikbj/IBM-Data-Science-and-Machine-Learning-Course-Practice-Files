name = "Shouvik Bajpayee"

print(name)
print(len(name))
print(name[1])
print(name[10])
print(name[0:7])
print(name[8:11])
print(name[::-1])  # reverses the string
print(name[::2])  # prints every second element
print(name[:10:2])  # prints every second value upto index 10
print(3 * name)
print("Shouvik\nBajpayee")
print("Shouvik\\Bajpayee")
print(r"Shouvik\Bajpayee")  # prints raw string without escaping any character

print(name.upper())
print(name.lower())

print(name.replace('Bajpayee', 'Baaj'))

print(name.find('Baj'))  # prints start index of 'Baj' else -1
