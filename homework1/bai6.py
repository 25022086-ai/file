# Bài 6. Nhập vào 3 số a, b, c. Kiểm tra xem đây có phải là cạnh của 1 tam giác không,
# nếu đúng thì tính diện tích của tam giác đó, in ra với 1 chữ số phần thập phân, nếu nó
#  không phải 3 cạnh của tam giác thì in ra “Khong phai 3 canh cua tam giac”.
a=list(map(float,input('nhập độ dài 3 cạnh a,b,c=').strip().split()))
if abs(a[0] - a[1])>a[2] or abs(a[1]- a[2])>a[0] or abs(a[0]- a[2])>a[0] :
    print('Khong phai 3 canh cua tam giac')
else:
    s1=a[0]+a[1]+a[2]
    s2=s1/2
    s3=(s2*(s2-a[0])*(s2-a[1])*(s2-a[2]))**0.5
    print('diện tích tam giác :'+f"{s3:.1f}")