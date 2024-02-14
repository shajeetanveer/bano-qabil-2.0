'''Python Program to Demonstrate initiating a Class'''
class Human:
    # A Sample Method
    attr1 = "Human"
    attr2 = "Student"
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a",self.attr2)
#Driver Code
#Object Initiation
Rodger = Human()

print(Rodger.attr1)
Rodger.fun()



