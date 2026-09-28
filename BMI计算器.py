"""这是一个BMI计算器"""
weight=float(input('请输入体重（单位：kg）:'))
height=float(input('请输入身高（单位：m）:'))
BMI=weight/(height**2)
print(f'您的BMI值是：{BMI}')
if BMI<18.5:
    print('偏瘦！')
elif 18.5<=BMI<24:
    print('正常！')
elif 24<=BMI<28:
    print('超重!')
else:
    print('肥胖！')