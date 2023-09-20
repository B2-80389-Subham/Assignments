class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        Vehicle.__init__(self, max_speed, mileage)
        self.seating_capacity = seating_capacity

    def display_info(self):
        print(f"Max Speed: {self.max_speed} km/h")
        print(f"Mileage: {self.mileage} km/l")
        print(f"Seating Capacity: {self.seating_capacity} passengers")


my_bus = Bus(80, 6, 50)
my_bus.display_info()
