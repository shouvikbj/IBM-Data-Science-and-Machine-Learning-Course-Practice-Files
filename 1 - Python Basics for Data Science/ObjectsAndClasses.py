# python objects and classes
class Person:
    # below function is the constructor
    def __init__(self, name, address):
        self.name = name
        self.address = address

    # below is a class method
    def getName(self):
        return self.name

    # below is a class method
    def getAddress(self):
        return self.address

    # below is a class method
    def changeName(self, newName):
        self.name = newName

    # below is a class method
    def changeAddress(self, newAddress):
        self.address = newAddress


shouvik = Person("Shouvik", "Kanakpur")

name = shouvik.getName()
print(name)
address = shouvik.getAddress()
print(address)

shouvik.changeName("Shouvik Bajpayee")
shouvik.changeAddress("Bahargram, Panskura(R.S.)")

newName = shouvik.getName()
print(newName)
newAddress = shouvik.getAddress()
print(newAddress)

# Below is example of inheritance


class Student(Person):
    def __init__(self, name, address, dgpa):
        self.dgpa = dgpa
        self.name = name
        self.address = address

    def getDgpa(self):
        return self.dgpa


baj = Student("Baaj", "Serampore", 8.5)

print(baj.getName())
print(baj.getAddress())
print(baj.getDgpa())

baj.changeName("Moni")
baj.changeAddress("Maniktolla")

print(baj.getName())
print(baj.getAddress())
print(baj.getDgpa())
