with open('d:/code/file/input.txt','r',encoding='utf-8') as f_in:
    number=f_in.read().split()
    n1=int(number[0])
    n2=int(number[1])
    n3=int(number[2])
if n1%2==0:
    print('chẵn')
else:
    print('lẻ')