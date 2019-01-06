# 就是Import
# 随机生成10个数。
import random

# i = 1
#
# while i <= 10:
#     rand_int = random.randint(1, 100)
#     print(i, rand_int)
#     i = i + 1

start = input('请输入要猜数字最小值：')
end = input('请输入要猜数字最小值：')
start = int(start)
end = int(end)

num_guess = random.randint(start, end)
count = 0
print('要猜的数字是：', num_guess)
while True:
    count = count + 1
    user_guess = input('请猜数字：')
    user_guess = int(user_guess)
    if user_guess == num_guess:
        print('猜对了')
        print('这是猜的第', count, '次')
        break
    elif user_guess > num_guess:
        print('数字要小一点点')
    elif user_guess < num_guess:
        print('数字要大一点点')
    else:
        print('请输入正确的数字。')
    print('这是猜的第', count, '次')
