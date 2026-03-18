with open('d:/code/file/input.txt','r',encoding='utf-8') as f_in:
    number=[int(x) for x in f_in.read().split()]
    k=len(number)
    m=number[0]
    for i in range(0,k):
        if number[i]>m:
            m=number[i]
print(m)