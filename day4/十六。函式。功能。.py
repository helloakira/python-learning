# 函式收纳程序码。是个功能。
# def = define 使用wash().用到函数就要空两行。
# 函式就是投币口，参数就是投币。
# 写参数的时候，等号左右不用空格。

# 回传return
# 有return 可以把东西定义一下存下来。
# 除号自动转成浮点数。


def wash(dry, water=555):
    print('开机')
    print('加水', water)
    print('旋转')
    if dry:
        print('烘干')
    print('关机')


wash(True)
wash(False)
wash(False, 999)
wash(water=666, dry=True)


def average(list_average):
    result = sum(list_average) / len(list_average)
    return result


result_1 = average([21312, 432423, 423432])
result_2 = average([12, 4123, 24212])
result_3 = average([86312, 672423, 76432])

print(result_1, result_2, result_3)


