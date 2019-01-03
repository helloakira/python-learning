# while就是当。。。执行。

# x = 9
# y = 1
# while x < 15:   # while True/False:
#     print(y, '小于15继续走')
#     print('loop to loop')
#     x = x + 1
#     y += 1
# print('x的值：', x)

while True:
    print('跑出去！')
    break   # 出去loop
print('已跑出去！')

# 输入判断。

while True:
    mode = input('请输入模式：')  # 输入的时候写进来，不然会重复。
    if mode == 'q':
        print('游戏结束')
        break
    elif mode == '1':
        print('启动游戏模式一')
    elif mode == '2':
        print('启动游戏模式二')
    else:
        print('请输入1/2/q')

