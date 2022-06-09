def uscln(a, b):
    temp1 = a;
    temp2 = b;
    while (temp1 != temp2):
        if (temp1 > temp2):
            temp1 -= temp2;
        else:
            temp2 -= temp1;
    uscln = temp1;
    return uscln;

def bscnn(a, b):
    return int((a * b) / uscln(a, b));

a = int(input("Nhập số nguyên dương a = "));
b = int(input("Nhập số nguyên dương b = "));

print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b));
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", bscnn(a, b));
