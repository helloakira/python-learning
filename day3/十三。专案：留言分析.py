# 余数 % 1000 == 0 可以弄到1000 2000精准的余数。
# for 就像一帧一帧的游戏。

data = []
count = 0

sum_len = 0

with open('../053 reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count = count + 1
        if count % 100000 == 0:
            print(len(data))

print('该评论读取完毕，总共有', len(data), '条评论')
print('第一个评论：', data[0])

# 弄平均字段

for review in data:
    sum_len = sum_len + len(review)

review_average = sum_len / len(data)
print('每笔留言平均字段数量为', review_average)

# 筛选字段
# 你想干啥。先弄一个空列表。
review_down100 = []
review_up100 = []

for review in data:
    if len(review) <= 100:
        review_down100.append(review)
    else:
        review_up100.append(review)
print('小于100个字的有：', len(review_down100), '条')
print('大于100个字的有：', len(review_up100), '条')

review_good = []
review_bad = []

for review in data:
    if 'good' in review:
        review_good.append(review)
    elif 'bad' in review:
        review_bad.append(review)

print('好的有：', len(review_good), '条')
print('不好的有：', len(review_bad), '条')

# 快写法
# 进阶写法
# 列表 = [.append(要写这个) for review in data if 'good' in review]
# 装个1试试
# 前面放d比较多。

review_well = [d for d in data if 'well' in d]
print('好的有：', len(review_well), '条')

review_1 = [1 for d in data if 'bad' in d]
print('不好的有用1表示：', review_1)

review_TF = ['bad' in d for d in data]
print('bad用布尔表示：', review_TF)



