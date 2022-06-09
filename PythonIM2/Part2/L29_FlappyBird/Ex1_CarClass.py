class Car:
    # thuộc tính đối tượng
    def __init__(self, tenxe, mausac, nguyenlieu):
        self.tenxe = tenxe
        self.mausac = mausac
        self.nguyenlieu = nguyenlieu

    #phương thức in thông tin của xe
    def print_info(self):
        print('Tên xe là', self.tenxe)
        print('Xe có màu', self.mausac)
        print('Xe sử dụng nguyên liệu là', self.nguyenlieu)

# tạo đối tượng
toyota = Car("Toyota", "Đỏ", "Điện")
lamborghini = Car("Lamborghini", "Vàng", "Diesel")
porsche = Car("Porsche", "Xanh", "Gas")

# gọi phương thức
toyota.print_info()
lamborghini.print_info()
porsche.print_info()