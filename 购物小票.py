"""这是一个用来模拟购物小票的程序"""
the_1st_product = "无线鼠标"
PRICE = 12.5
buy_quantity = int(input('请输入要购买商品的数量：'))
TEX_RATE = 0.13
total_price=PRICE*buy_quantity*(1 + TEX_RATE)
print('=========购物小票=========')
print(f'商品：{the_1st_product}')
print(f'税率：{TEX_RATE}' )
print(f'数量: {buy_quantity}')
print(f'价格：{total_price}' )
print('=========================')