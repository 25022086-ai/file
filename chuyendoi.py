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
print(chuyendoi(a))