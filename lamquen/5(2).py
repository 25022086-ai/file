with open('d:/code/file/input.txt','r',encoding='utf-8') as f_in:
    number=f_in.read().split()
    k=len(number)
    m=int(number[0])
    i=0
    while i<k:
        if m<int(number[i]):
            m=int(number[i])
        i=i+1
print (m)