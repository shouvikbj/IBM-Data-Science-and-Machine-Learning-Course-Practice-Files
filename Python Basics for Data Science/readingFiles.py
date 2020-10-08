import os

# getting the absolute path of the "data.txt" file
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

print("\n")

# reading data from the file
text_file = open(f"{APP_ROOT}/data.txt", "r")
print(text_file.read())
text_file.close()

print("\n")

# writing new data into the file overwriting old data
text_file = open(f"{APP_ROOT}/data.txt", "w")
data = input("Write something: ")
text_file.write(f"{data}\n")
text_file.close()

print("\n")

# reading the newly entered data from the file
text_file = open(f"{APP_ROOT}/data.txt", "r")
print(text_file.read())
text_file.close()

print("\n")

# appending new data at the end of the existing data
text_file = open(f"{APP_ROOT}/data.txt", "a")
data = input("Write some more: ")
text_file.write(f"{data}\n")
text_file.close()

print("\n")

# reading the new data from the file
text_file = open(f"{APP_ROOT}/data.txt", "r")
print(text_file.read())
text_file.close()

print("\n")