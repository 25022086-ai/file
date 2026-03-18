# Bài 5: Nhập vào chữ cái hoa A, in ra chữ cái thường liền trước chữ cái a thường tương
# ứng của A. Xét TH khi c = ‘A’ là đặc biệt. 
l=input('nhập một chữ cái in hoa:')
def chuyen(a):
    return chr(ord(a)+31)
print(chuyen(l))