# file: network.py
from abc import ABC, abstractmethod

class INetworkable(ABC):
    # Em khong biet khai bao thuoc tinh (property) trong interface Python the nao cho chuan
    # nen em quy uoc cac class con phai tu co bien ipAddress va isConnected
    
    @abstractmethod
    def Connect(self, ipAddress):
        pass
        
    @abstractmethod
    def Disconnect(self):
        pass

'''
CÂU TRẢ LỜI LÝ THUYẾT:
Em chọn phương án "Tách NetworkPrinter kế thừa từ Printer và thực thi INetworkable".
Giải thích trade-off:
- Ưu điểm: Mô hình này giúp phân biệt rõ máy in thường và máy in mạng, tránh việc máy in thường gọi hàm Connect() rồi báo lỗi. Đảm bảo nguyên lý thiết kế không ép class con nhận những phương thức nó không dùng tới.
- Nhược điểm (Trade-off): Nếu sau này có thêm nhiều loại thiết bị mạng (máy chiếu mạng, máy scan mạng...), số lượng class sẽ bị nhân lên rất nhiều (class explosion), và code kết nối mạng (Connect, Disconnect) phải viết lặp lại ở nhiều nơi.
'''