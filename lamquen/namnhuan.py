with open('input.txt','r',encoding='utf-8') as f_in:
    year=float(f_in.read())
    if year%4==0:
        print(' năm nhuận')
    else:
        print('ko phai nam nhuận')