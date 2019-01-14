# 读取
def read_file(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        lines = []
        for line in f:
            lines.append(line.strip('\n'))
        return lines


# 转换
def convert(lines):
    for line in lines:
        s = line.split(' ')
        time = s[0][:5]
        name = s[0][5:]
        print('时间：', time)
        print('名称：', name)


# 合成main
def main():
    lines = read_file('3.txt')
    convert(lines)
    # write_file('output.txt', chat)


main()