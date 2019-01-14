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

word_count = {}

for d in data:
    words = d.split(' ')
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

for word in word_count:
    if word_count[word] > 1000000:
        print(word, word_count[word])

print(len(word_count))
print(word_count['Tom'])

while True:
    user_word = input('请问你要查的字？')
    if user_word == 'q':
        break
    if user_word in word_count:
        print(user_word, '出现的次数为', word_count[user_word])
    else:
        print('没有出现过这个字')
print('感谢使用')






