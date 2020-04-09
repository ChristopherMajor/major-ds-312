class Auto():
    def __init__(self, color, num_wheels, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.num_wheels = num_wheels

    def drive(self):
        print('we are driving', self.model)

    def advertise(self):
        print('BUY OUR', self.model)

class Truck(Auto):
    def __init__(self, color, num_wheels, make, model, year, bed_size):
        super().__init__(color, num_wheels, make, model, year)
        self.bed_size = bed_size
    
    def advertise(self):
        print('SUNDAY SUNDAY SUNDAY', self.model)

if __name__ == '__main__':
     car = Auto('Blue', 4, 'Toyota', 'Prius', 2020)
     car.drive()
     car.advertise()
     car2 = Auto('Black', 4, 'Tesla', 'Model-S', 2019)
     car2.drive()
     
     truck = Truck('Silver', 4, 'Tesla', 'Cybertruck', 2020, bed_size='long')
     truck.drive()
     print(truck.bed_size)
     truck2 = Truck('Red', 4, 'Ford', 'F150', 2018, bed_size='short')
     truck2.drive()
     print(truck2.bed_size)
     truck2.advertise()
