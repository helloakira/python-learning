# 读取
def read_file(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        lines = []
        for line in f:
            lines.append(line.strip('\n'))
        return lines


# 转换
def convert(lines):
    chat = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            chat.append(person + ' : ' + line + '\n')
    return chat


# 输出
def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line)


# 合成main
def main():
    lines = read_file('input.txt')
    print(lines)

    chat = convert(lines)
    print(chat)

    write_file('output.txt', chat)


main()