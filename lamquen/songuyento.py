import math    
with open('input.txt','r',encoding='utf-8') as f_in:
    n=float(f_in.read())
i= math.sqrt(n)
a=True
if n<2:
    a=False
else:
    for k in range(2,int(math.sqrt(n))+1):
        if n%k==0:
            a=False
            break
if a:
    print('so nguyen to')
else:
    print('kh phai so nguyen to')