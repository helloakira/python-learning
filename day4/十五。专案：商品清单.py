# 反正都要while True总不会错。
# 二维清单就是清单中的清单。
# 快写可以直接写 p = [name, price]
# 打印一下他们是什么。

# 字符串可以加法 乘法
# f.write写东西。写在当前目录，没有的就创建。有的就覆盖。
# \n换行
# ,对于csv可以隔个格子。

# 在csv增加标题。商品，价格。
# 用到中文就要在后面加 open（ encoding = 'utf-8'）
# excel导入的时候用UTF-8导入。
# comma就是逗点。

# 读取CSV数据。
# 切割。就是每一行.split('切割的字符串'),切完变成列表。  每一行.strip（）就是去除\n
# 快写。储存。name, price =

# continue break都是循环才可以用。但是continue不会退出循环。
# 一般使用在FOR LOOP最上面

# import os 就是operating system作业系统。相当于政府。
# os.path.isfile('地址/档名')

import os

products = []

# 读取数据,检查档案。
if os.path.isfile('products.csv'):
    print('找到档案')
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,价格' in line:
                continue
            List = line.strip().split(',')
            name = List[0]
            price = List[1]
            products.append([name, price])
else:
    print('找不到档案')

print(products)

# 输入数据
while True:
    name = input('请输入名称：')
    if name == 'q':
        break
    price = input('请输入价格：')
    price = int(price)
    # p = []
    # p.append(name)
    # p.append(price)
    products.append([name, price])

print(products)

# 打印清单
for p in products:
    print(p[0], '的价格是', p[1])


# 写入到文档
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,价格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')

