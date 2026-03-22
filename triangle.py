def bool_tri(a,b,c):
    if abs(a+b)>c and abs(a+c)>b and abs(b+c)>a:
        return True
    else:
        return False
def type_tri(a,b,c):
    if a==b or a==c or b==c:
        if a==b and a==c and b==c:
            s= "Tam giác đều"
        else:            
            s= "Tam giác cân"
    elif a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
        s= "Tam giác vuông"
    else:        s= "Tam giác thường"
    return s
