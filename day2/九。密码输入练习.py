# 输入密码但是有机会次数。
password = 'a123456'
chance = 3
while chance > 0:
    chance = chance - 1
    user = input('请输入密码：')
    if user == password:
        print('登录成功')
        break   # 逃出循环
    else:
        if chance != 0:
            print('登录失败,机会还有', chance, '次')
        else:
            print('没机会尝试，要锁账号！')

