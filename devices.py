




from models import Device
import datetime

class Computer(Device):
    def __init__(self, device_id, name, year, price, ram, cpu, has_gpu):
        super().__init__(device_id, name, year, price)
        self.ram = ram
        self.cpu = cpu
        self.has_gpu = has_gpu

    def CalculateAnnualMaintenanceCost(self):
        cost = self.price * 0.05
        
        if self.has_gpu == True: 
            cost += self.price * 0.02
            
        tuoi_doi = datetime.datetime.now().year - self.year
        if tuoi_doi > 5:
            cost += self.price * 0.01
            
        return cost

class Printer(Device):
    def __init__(self, device_id, name, year, price, type_printer, pages, is_color):
        super().__init__(device_id, name, year, price)
        self.type_printer = type_printer
        self.pages = pages
        self.is_color = is_color 

    def CalculateAnnualMaintenanceCost(self):
        cost = self.price * 0.04
        
        if self.pages > 100000:
            cost = cost + 500000
            
        if self.is_color == True:
            cost = cost + 300000
            
        return cost

class Projector(Device):
    def __init__(self, device_id, name, year, price, brightness, lamp_hours, resolution):
        super().__init__(device_id, name, year, price)
        self.brightness = brightness
        self.lamp_hours = lamp_hours
        # Giai thich: May chieu can biet do phan giai (vd 1080p, 4K) vi no phan anh chat luong va gia linh kien thay the.
        self.resolution = resolution 

    def CalculateAnnualMaintenanceCost(self):
        cost = self.price * 0.03
        if self.lamp_hours > 3000:
            cost += 1500000
        return cost