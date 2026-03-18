# Bài 8: Nhập vào họ tên chủ hộ và chỉ số điện kế tháng trước và chỉ số điện kế tháng này,
# tính tiền điện tháng này cho hộ biết:
# - Từ 0 – 50kWh: 1.984 đồng/kWh
# - Bậc 2: Từ 51 – 100 kWh: 2.050 đồng/kWh
# - Bậc 3: Từ 101 – 200 kWh: 2.380 đồng/kWh
# - Bậc 4: Từ 201 – 300 kWh: 2.998 đồng/kWh
# - Bậc 5: Từ 301 – 400 kWh: 3.350 đồng/kWh
# - Bậc 6: Từ 401 trở đi kWh: 3.460 đồng/kWh 
name=input('tên chủ hộ :')
a1=input('chỉ số điện cuối tháng trước :')
a2=input('chỉ số điện cuối tháng này :')
s1=int(a2)-int(a1)
if s1<0:
    print('Dữ liệu không đúng')
elif s1<= 50:
    print('Họ và tên :'+name)
    print(f"{s1*1984*1.08:.0f}")
elif 50<s1<=100:
    print('Họ và tên :'+name)
    print(f"{(50*1984+(s1-50)*2050)*1.08:.0f}")
elif 100<s1<=200:
    print('Họ và tên :'+name)
    print(f"{(50*1984+50*2050+(s1-100)*2380)*1.08:.0f}")
elif 200<s1<=300:
    print('Họ và tên :'+name)
    print(f"{(50*1984+50*2050+100*2380+(s1-200)*2998)*1.08:.0f}")
elif 300<s1<=400:
    print('Họ và tên :'+name)
    print(f"{(50*1984+50*2050+100*2380+100*2998+(s1-300)*3350)*1.08:.0f}")
else:
    print('Họ và tên :'+name)
    print(f"{(50*1984+50*2050+100*2380+100*2998+3350*100+(s1-400)*3460)*1.08:.0f}")