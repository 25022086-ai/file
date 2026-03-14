# Bài 2: Một khu đất hình chữ nhật có chiều rộng a, chiều dài b. Người ta xây một khu
# vui chơi hình tròn tại vị trí trung tâm khu đất như hình vẽ. Nhập vào a, b. Hãy tính phần
# diện tích còn để trồng cây xung quanh là bao nhiêu. Biết pi = 3.14, lấy kết quả đến 2
# chữ số phần thập phân. 
a,b =map(int,input().split())
pi=3.14
s1=pi*(a/2)**2
s2=a*b
print(f"{s2-s1:.2f}")