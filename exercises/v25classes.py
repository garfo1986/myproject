# to start a class, we start we "class" and then naming the class, classes start with capital letters, brakets and colon.

class Car():
 # classes have state, propierties and behaviour (methods).
    largechasis =250 # this is a property
    widechasis = 120
    wheels = 4
    running = False # it means all cars we create from this class will start as off
#methods: "def" "function name" "self" self is 
    def start(self):
        self.running=True

    def state(self):
        if (self.running):
            return "the car is running"
        else:
            return "the car is stopped"


#then we can created objects, starting with a name:

mycar = Car() #we add the name of the object and then the name of the class where it belongs

# once we have created the object we can access to its properties by using a dot and the name  of the property.

print(mycar.largechasis) #this prints "250" as we created it in class
print(("my car's lenght"), mycar.widechasis)
print (("my car has "), mycar.wheels, ( "wheels"))
mycar.start() #self.running will change to True
print(mycar.state())
