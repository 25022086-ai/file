# 1. Trò chơi Đoán số (Number Guessing Game)
# Mô tả: Chương trình sẽ tạo ra một số ngẫu nhiên từ 1 đến 100. Người chơi sẽ nhập dự đoán của mình.
# Sau mỗi lần đoán, chương trình sẽ gợi ý số cần tìm là "Lớn hơn" hay "Nhỏ hơn" số vừa đoán cho đến 
# khi người chơi đoán trúng.
# Kỹ năng luyện tập: Vòng lặp while, điều kiện if/else, thư viện random.
import random    #thư viện random
ran_num=random.randint(1,100)
number=int(input('Bạn có 5 lần đoán ,hãy nhập một số mà bạn dự đoán là đúng:'))
i=5
if(ran_num==number):                            #kiểm tra lần đầu 
    print('bạn đã đoán đúng !')                 #in ra nếu đúng luôn
else:                                           #tiếp tục cho người chơi đoán
    while ran_num!=number and i>1:              #vòng lặp kiểm tra đáp án người chơi chọn
        i=i-1                                   #giảm số lần đoán của người chơi
        if ran_num<number:                      #kiểm tra số
            number=int(input(f'Bạn còn {i} lần đoán, hãy nhập một số nhỏ hơn: '))
        else:
            number=int(input(f'bạn còn {i} lần đoán, hãy nhập một số lớn hơn :'))
if i>0 and ran_num==number :                    #in ra 
    print(f'bạn đã đoán đúng !, đáp án là {ran_num}')
else:
    print(f'chúc may mắn lần sau, đáp án là {ran_num}')