# CHÀO MỪNG ĐẾN VỚI TRÒ CHƠI THÁM HIỂM
print('Chào mừng đến với trò chơi "THÁM HIỂM KHU RỪNG BÍ ẨN"')
name = input("Bạn tên là gì? ")
print("Chào mừng", name+"! " +"Bắt đầu thám hiểm nhé!")
print()
print("Bạn thức dậy trong một khu rừng và không biết mình đang ở đâu.")
print("Bạn nhìn thấy một con sông bên phải và một lâu đài bí ẩn bên trái.")
ans1 = input("Bạn sẽ đi đâu? T/P ?").lower()
print()
#print(ans1)
while ans1 not in ["t", "p"] :
    ans1 = input("Bạn hãy nhập 't' hoặc 'p'").lower()
if ans1 == "t":
    print("Bạn đi thẳng tới lâu đài bí ẩn mà không một chút do dự.")
    print("Trước mặt bạn là một cánh cổng lớn")
    print("Bạn đẩy cánh cổng mở ra và bạn nhìn thấy 2 con đường, bên trái vàbên phải.")
    ans1_1 = input("Bạn sẽ chọn đi con đường nào? T/P ?").lower()
    print()
    while ans1_1 != "t" and ans1_1 != "p":
        ans1_1 = input("Bạn hãy nhập 't' hoặc 'p'").lower()
    if ans1_1 == "t":
        print("Bạn tìm thấy một đống vàng và trang sức.")
        print("Chúc mừng bạn! Bạn đã trở thành người giàu có!")
        print("KẾT THÚC")
    else:
        print("Bạn đi xuống một đường hầm tối đen.")
        print("Và bạn không thể nhìn thấy bất cứ thứ gì cho đến khi có mộtđám lửa đi thẳng về phía bạn." )
        print("Thật không may! Bạn đã bị thiêu sống.")
        print("KẾT THÚC")
else:
    print("Bạn đến bên bờ hồ và hớp vài ngụm nước, bạn cảm thấy tỉnh táohơn.")
    print("Đằng xa phía trên trái, bạn nhìn thấy một ngôi làng.")
    print("Phía bên phải, bạn nhìn thấy một ông lão đang thu hoạch thảo mộcgần căn lều." )
    ans1_2 = input("Bạn sẽ chọn đi hướng nào, T/P? ").lower()
    print()
    if ans1_2 == "t":
        print("Bạn đi thẳng tới ngôi làng.")
        print("Bạn bắt đầu một cuộc sống bình thường mới như một người nôngdân ở đây.")
        print("KẾT THÚC")
    else:
        print("Bạn đi thẳng về phía ông lão." )
        print("Ông ta đang lẩm bẩm một điều gì đó." )
        print("Thật đáng tiếc! bạn đã biến thành một con ếch.")
        print("KẾT THÚC")