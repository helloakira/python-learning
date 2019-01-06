# 1.with open('文件', 'r') as 命名。
# 2.'r'就是read 命名一般用f就好。
# 3.cmd cls可以清屏。
# 4.打印出隐藏的\n
# 5.去掉换行符号。字符串.strip() 几乎打开档案都得用。
# 6.清单.append()
# 7.with可以自动close
# 8.打印f 多了个<_io.TextIOWrapper name='news.txt' mode='r' encoding='cp936'>
# 9.两条反斜杆，可以防止\n运行
# 10.用.strip()返回return 没有括号就是属性。

data = []
data_strip = []

with open('news.txt', 'r') as f:
    for new in f:
        print(new)
        data.append(new)
        data_strip.append(new.strip())

print('打印new.strip()：', new.strip())
print('打印\\n:', data)
print('打印\\n:', data_strip)
print('打印f：', f)




