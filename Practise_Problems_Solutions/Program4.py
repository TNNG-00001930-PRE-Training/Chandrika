class String:
    def __init__(self):
        self.input = " "

    def getString(self):
        self.input = input("Enter a string: ")

    def printString(self):
        print(self.input.upper())

def testString():
    update = String()
    update.getString()
    update.printString()

# Test the class methods
testString()