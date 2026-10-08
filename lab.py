# file: lab.py
import datetime
from models import DeviceStatus

class LabRoom:
    def __init__(self, room_id, name, capacity):
        self.room_id = room_id
        self.name = name
        self.capacity = capacity
        self.devices = [] 

    def AddDevice(self, device):
        # Khong chap nhan null
        if device is None:
            print("Loi: Khong the them thiet bi null")
            return
            
        # Check capacity
        if len(self.devices) >= self.capacity:
            print("Loi: Phong lab da day thiet bi")
            return
            
        # Khong them hai thiet bi cung ma
        for d in self.devices:
            if d.device_id == device.device_id:
                print(f"Loi: Thiet bi ma {device.device_id} da ton tai trong phong")
                return
                
        self.devices.append(device)
        print(f"Da them {device.name} vao phong {self.name}")

    def RemoveDevice(self, device_id):
        for d in self.devices:
            if d.device_id == device_id:
                self.devices.remove(d)
                return True
        return False

    def FindDevice(self, device_id):
        for d in self.devices:
            if d.device_id == device_id:
                return d
        return None

    def CalculateAnnualMaintenanceCost(self):
        tong_tien = 0
        for d in self.devices:
            # Tinh da hinh, cu goi ham CalculateAnnualMaintenanceCost ma khong can quan tam no la class nao
            tong_tien = tong_tien + d.CalculateAnnualMaintenanceCost()
        return tong_tien

    def GetDevicesRequiringMaintenance(self):
        danh_sach_bao_tri = []
        nam_hien_tai = datetime.datetime.now().year
        
        for d in self.devices:
            tuoi = nam_hien_tai - d.year
            # Thiet bi dang bao tri hoac dung tren 5 nam
            if d.status == DeviceStatus.UnderMaintenance or tuoi > 5:
                danh_sach_bao_tri.append(d)
                
        return danh_sach_bao_tri