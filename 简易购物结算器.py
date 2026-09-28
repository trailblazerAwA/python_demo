"""简易购物结算器"""
name=input('请输入商品名称:')
e_price=float(input('请输入商品单价:')) #可能按‘个’卖，也可能按‘斤’卖
number=float(input('请输入商品购买个数或斤数:'))
t_price1=e_price * number
print('========购物结算========')
print(f'你购买了{number}个' + name + f'单个（斤）为{e_price:.2f}元')
print(f'原价:{t_price1:.2f}元')
if t_price1 > 100:
    print('享受九折优惠！')
    t_price2 = (t_price1) * 0.9
else:
    t_price2 = t_price1
print(f'最终应付:{t_price2:.2f}元')
print('========================')