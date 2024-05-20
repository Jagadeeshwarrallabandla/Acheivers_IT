#Creating the class
class Bike:
    #intialising the constructor
    def __init__ (self,brand,name,model):
        self.brand = brand
        self.name = name
        self.model = model
    
    #Creating the methods to describe the behaviour of the Object
        
    def bike_details(self,topspeed):
        self.topspeed = topspeed
        return f"The New {self.brand} {self.name} {self.model} with a top Speed of {topspeed}"
    
    def bike_start(self):
        return f"The {self.brand} {self.name} {self.model} is Started"
    
    def bike_running(self,speed):
        self.speed = speed
        return f"{self.brand} {self.name} {self.model} running with a spped of {self.speed} Km/hr"
    
#Creating Instance
bike_features = Bike("Bajaj","Pulsar","N160")

#printing the Attributes
print(bike_features.brand)
print(bike_features.name)
print(bike_features.model)

#printing the methods
print(bike_features.bike_details(220))
print(bike_features.bike_start())
print(bike_features.bike_running(100))

#adding attributes
setattr(bike_features,"Color","Black")
print(bike_features.Color)

'''del bike_features.Color
print(bike_features.Color)'''


bike_features.engine_capacity = "160cc"
print(f"{bike_features.bike_details(220)} {bike_features.Color} color with a poweful Torque of {bike_features.engine_capacity }")

        
        
    