with open('d:/code/file/input.txt','r',encoding='utf-8') as f_in:
    number=f_in.read().split()
    n1=int(number[0])
    n2=int(number[1])
    n3=int(number[2])
    print('diện tích hình tròn 1=',3.14159*n1*n1,'chu vi hình tròn 2=',2*3.14159*n1)
