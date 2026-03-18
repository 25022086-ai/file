def chuyendoi(a):
    s=""
    match a:
        case 0:
            s="khong"
        case 1:
            s="mot"
        case 2:
            s="hai"
        case 3:
            s="ba"
        case 4:
            s="bon"
        case 5:
            s="nam"
        case 6:
            s="sau"
        case 7:
            s="bay"
        case 8:
            s="tam"
        case 9:
            s="chin"
    return s
a=int(input())
i=0
A=[]
while a>10:
    A.append(a%10)
    a=a//10
    i=i+1
A.append(a)
B=[]
for k in range(i,-1,-1):
    B.append(chuyendoi(A[k]))
C=" ".join(B)
print(C)