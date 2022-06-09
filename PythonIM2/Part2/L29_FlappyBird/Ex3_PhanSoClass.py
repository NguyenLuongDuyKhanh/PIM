class phanso:
    # thuộc tính đối tượng
    def __init__(self, tuso, mauso):
        self.tuso = tuso
        self.mauso = mauso

    #phương thức của đối tượng
    def nhan(self, tuso_a, mauso_a):
        print('Kết quả phép nhân là', self.tuso*tuso_a, '/',
        self.mauso*mauso_a)

    def chia(self, tuso_a, mauso_a):
        print('Kết quả phép chia là', self.tuso * mauso_a, '/',
        self.mauso * tuso_a)

# tạo đối tượng
a = phanso(2, 5)

# gọi phương thức
a.nhan(3, 4)
a.chia(1, 5)