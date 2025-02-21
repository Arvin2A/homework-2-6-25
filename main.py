class Car:
    def __init__(self,make,model,color):
        self.color = color #public attribute
        self.__make = make #private 
        self.__model = model #private 
        self.__speed = 0 #private 
    def accelerate(self,increase):
        self.__speed += increase
        return f"increases the speed by {self.__speed} miles per hour"
    def brake(self,decrease):
        if self.__speed - decrease <= 0:
            self.__speed = 0
            return f"The car came to a full stop"
        else:
            self.__speed -= decrease
        return f"decreases speed by {decrease} miles per hour, it is now at {self.__speed} mile per hour"

    def get_make_model(self): #public method
        return f"{self.__make} {self.__model}"
    def set_make(self, make):  # Missing setter for private __make
        self.__make = make
toyota = Car("Toyota","Corolla","White")
print(toyota)
print(toyota.get_make_model())
print(toyota.set_make("Honda"))
print(toyota.brake(10))