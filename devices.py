# file: devices.py
from models import Device
from network import INetworkable
import datetime

# May tinh luon co the ket noi mang
class Computer(Device, INetworkable):
    def __init__(self, device_id, name, year, price, ram, cpu, has_gpu):
        super().__init__(device_id, name, year, price)
        self.ram = ram
        self.cpu = cpu
        self.has_gpu = has_gpu
        
        self.ipAddress = ""
        self.isConnected = False

    def Connect(self, ipAddress):
        if ipAddress == "":
            print("Loi: Dia chi IP khong duoc rong")
            return
        if self.isConnected == True:
            print("Loi: Thiet bi dang ket noi roi, khong the ket noi lai")
            return
            
        self.ipAddress = ipAddress
        self.isConnected = True
        print(f"[{self.name}] Da ket noi mang voi IP: {self.ipAddress}")

    def Disconnect(self):
        self.isConnected = False
        self.ipAddress = "" # Khong con dia chi IP sau khi ngat
        print(f"[{self.name}] Da ngat ket noi mang.")

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

# Tach NetworkPrinter ke thua Printer va implement INetworkable
class NetworkPrinter(Printer, INetworkable):
    def __init__(self, device_id, name, year, price, type_printer, pages, is_color):
        super().__init__(device_id, name, year, price, type_printer, pages, is_color)
        self.ipAddress = ""
        self.isConnected = False

    def Connect(self, ipAddress):
        # Viet the nay cho khac cai may tinh mot chut (kieu sinh vien copy paste roi sua)
        if ipAddress != "" and self.isConnected == False:
            self.ipAddress = ipAddress
            self.isConnected = True
            print(f"[{self.name}] May in mang da ket noi: {self.ipAddress}")
        else:
            print("Loi: IP rong hoac may in dang ket noi")
            
    def Disconnect(self):
        self.isConnected = False
        self.ipAddress = ""
        print(f"[{self.name}] May in da ngat mang.")

class Projector(Device):
    def __init__(self, device_id, name, year, price, brightness, lamp_hours, resolution):
        super().__init__(device_id, name, year, price)
        self.brightness = brightness
        self.lamp_hours = lamp_hours
        self.resolution = resolution 

    def CalculateAnnualMaintenanceCost(self):
        cost = self.price * 0.03
        if self.lamp_hours > 3000:
            cost += 1500000
        return cost