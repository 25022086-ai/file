a=float(input("a="))
b=float(input("b="))
if(a==0):
    if(b==0):
        print('phương trình vô số nghiệm')
    else:
        print('phương trình vô nghiệm')
else:
    print('x=',-b/a)