# ：就是“的话”
# work = input('炮叔是否要加班：')

# if work == '加班':
#     print('窝家玩18R')
#     print('玩怪猎')
#     print('玩求生之路2')
# else:
#     print('去看电影')
#     print('出去吃饭')

# age = input('请输入年龄：')
# age = int(age)  # 转换Casting
# adult = '是个成年人。'
# un_adult = '未成年无法预览'
#
# if age >= 18:
#     print(adult)
# else:
#     print(un_adult)

# 一分多路
# 另外如果else if
# 而且and
point = input('请输入成绩：')
point = int(point)

if point < 60:
    print('不及格')
elif 60 <= point < 80:
    print('及格')
elif 80 <= point < 90:
    print('良好')
else:
    print('优秀')
