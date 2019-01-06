# 1.索引index 0 1 2 3 4 5 6
# 2.引用[0]
# 3.用.append可以加入列表的功能。列表.append
# 4.那个.就是“的”的意思。
# 5.len就是length的简写。可以看列表的长度。len(列表)
# 6.判断语句in 返回True False 变成了是非题 "字符串" in 列表

cars = ['Toyota', 'Benz', 'LEXUS']

print('索引[201]：', cars[2], cars[0], cars[1])

cars.append('Honda')
print('用.append（之后）：', cars)
# print(cars.append('Honda')) 返回none

print('用len(cars)：', len(cars))
print('用.__len__()', cars.__len__())

# 7.for loop就是将清单的东西一个一个拿出来。
好多车 = cars
for 一辆车 in 好多车:
    print('for用法：', 一辆车)

# 8.字符串也可以当清单 for 字符串。
# 9.什么len(清单) 一个字 in 清单都可以用。
交流 = 'Communication'

for 字母 in 交流:
    print('字符串清单用法：', 字母)

print('确定muni在不在里面：', 'muni' in 交流)
print('确定cp在不在里面：', 'cp' in 交流)