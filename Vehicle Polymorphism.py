class BMV:
    def __init__(self, model, top_speed):
        self.brand = 'BMW'
        self.model = model
        self.top_speed = top_speed
    def carinfo(self):
        print("Brand -", self.brand, "Model -", self.model)
    def fuel_type(self):
        print("The car normally uses Petrol")
    def max_speed(self):
        print("It has a max speed of 311 km/h with M Drivers Package")
class Ferrari:
    def __init__(self, model, top_speed):
        self.brand = 'Ferrari'
        self.model = model
        self.top_speed = top_speed
    def carinfo(self):
        print("Brand -", self.brand, "Model -", self.model)
    def fuel_type(self):
        print("The car normally uses High-Octane Petrol")
    def max_speed(self):
        print("It has a max speed of 339 km/h")
def car_performance(car_object):
    car_object.carinfo()
    car_object.fuel_type()
    car_object.max_speed()
BMVM8 = BMV(model = "M8 Coupe Competition", top_speed = "311 km/h with M Drivers Package")
FerrariSF90 = Ferrari(model = "SF90 XX StradaleAsseto", top_speed = "339 km/h")
all_cars = [BMVM8, FerrariSF90]
for each_car in all_cars:
    car_performance(each_car)