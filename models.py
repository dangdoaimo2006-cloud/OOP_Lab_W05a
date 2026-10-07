from abc import ABC, abstractmethod
from enum import Enum
import datetime

# Enum cho trang thai thiet bi
class DeviceStatus(Enum):
    Active = "Active"
    UnderMaintenance = "UnderMaintenance"
    Retired = "Retired"

class Device(ABC):
    def __init__(self, device_id, name, year, price):
        # Ma thiet bi khong duoc rong
        if device_id == "" or device_id is None:
            raise ValueError("Loi: Ma thiet bi khong duoc rong")
            
        # Ma thiet bi chi duoc thiet lap khi khoi tao
        self.device_id = device_id 
        self.name = name
        
        # Nam khong lon hon nam hien tai
        current_year = datetime.datetime.now().year
        if year > current_year:
            print("Canh bao: Nam su dung sai. Tu dong set ve nam hien tai.")
            self.year = current_year
        else:
            self.year = year
            
        # Gia mua lon hon 0
        if price <= 0:
            print("Canh bao: Gia mua phai lon hon 0. Tam de 100000.")
            self.price = 100000
        else:
            self.price = price
            
        self.status = DeviceStatus.Active
        
    @abstractmethod
    def CalculateAnnualMaintenanceCost(self):
        pass
        
    def __str__(self):
        return f"[{self.device_id}] {self.name} (Nam: {self.year}) - Trang thai: {self.status.value}"