class MyClass:
    def __init__(self):
        self.myInt = 0
        self.myBool = False
        self.myString = ""
    def myFunction(self, myParam):
        if self.myBool:
            for i in range(myParam):
                self.myInt += 1
        else:
            while self.myInt < myParam:
                self.myInt += 1