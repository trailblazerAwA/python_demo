weight=float(input('请输入快件重量(单位：kg)：'))
if weight<=1:
    print('运费为8元！')
elif 1<weight<=5:
    cost1=8+(weight-1)*3
    print(float(cost1))
elif 5<weight<=10:
    cost2=8+4*3+(weight-5)*2
    print(float(cost2))
elif weight>10:
    cost3=8+43+52+(weight-10)*1
    print(float(cost3))
else:
    print('重量输入错误，必须大于0！')
