# Bài 4: Viết chương trình nhập vào một “kí tự”, Kiểm tra xem c có phải là kí tự chữ cái
# không (hoa hoặc thường). Nếu đúng thì in ra “{c} là kí tu alphabet”, nếu sai in ra “{c}
# không phải là kí tự alphabet.
letter=input()
if 'a'<=letter<='z' or 'A'<=letter<='Z':
    print('{'+letter+'} là kí tu alphabet')
else:
    print('{'+letter+"} không phải là kí tự alphabet")