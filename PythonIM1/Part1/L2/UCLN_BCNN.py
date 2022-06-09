"""
 * Tìm ước số chung lớn nhất (USCLN)
 *
 * @param a: số nguyên dương
 * @param b: số nguyên dương
 * @return USCLN của a và b
"""
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

"""
 * Tìm bội số chung nhỏ nhất (BSCNN)
 *
 * @param a: số nguyên dương
 * @param b: số nguyên dương
 * @return BSCNN của a và b
"""
def bscnn(a, b):
    return int((a * b) / uscln(a, b));

a = int(input("Nhập số nguyên dương a = "));
b = int(input("Nhập số nguyên dương b = "));
#tính USCLN của a và b
print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b));
#tính BSCNN của a và b
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", bscnn(a, b));
