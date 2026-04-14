def kt_snt(a):
    if a<2:
        return False
    else:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return False
        return True
def kt_scp(a):
    n=int(a**0.5)
    if n*n==a:
        return True
    else:
        return False