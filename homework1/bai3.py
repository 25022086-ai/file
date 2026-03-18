# Bài 3: Viết chương trình nhập vào một “kí tự” c, nếu nó là chữ hoa thì in ra chữ thường
# tương ứng và ngược lại nếu nó là chữ thường thì in ra chữ hoa tương ứng của nó. (xem
# trước cấu trúc lựa chọn: if….else, ma)
str=input('Điền vào 1 ký tự:')
if 'z'>=str>='a':
    print(str.upper())
if 'Z'>=str>='A':
    print(str.lower())