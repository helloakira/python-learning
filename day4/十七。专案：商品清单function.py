# def先框起来。
# 文件名建议用参数控制。
# 有return就得用=存下来。
# 传参数进入，转换成什么什么。
# 只有一两行的就不要用function了。直接写就好。
# main()就是一堆function的大佬。
# 就是main（）不要带参数。

import os


# 读取数据,检查档案。
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,价格' in line:
                continue
            read_list = line.strip().split(',')
            name = read_list[0]
            price = read_list[1]
            products.append([name, price])
    return products


# 输入数据
def user_input(products):
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
    print('第一步让用户输入数据回传：', products)
    return products


# 打印清单
def print_products(products):
    for p in products:
        print(p[0], '的价格是', p[1])


# 写入到文档
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,价格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('找到档案')
        products = read_file(filename)
    else:
        print('找不到档案')
    print('第一步读文件回传：', products)
    products = user_input(products)
    print_products(products)
    write_file(filename, products)


main()