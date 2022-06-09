class Rectangle:
    # thuộc tính đối tượng
    def __init__(self, chieudai, chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong

    #phương thức của đối tượng
    def chuvi(self):
        self.P = (self.chieudai + self.chieurong) * 2
        print('Chu vi hình chữ nhật là', self.P)

    def dientich(self):
        self.S = self.chieudai * self.chieurong
        print('Diện tích hình chữ nhật là', self.S)

# tạo đối tượng
a = Rectangle(10, 5)

# gọi phương thức
a.chuvi()
a.dientich()