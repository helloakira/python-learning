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
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0

    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]

        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for msg in s[2:]:
                    allen_word_count += len(msg)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for msg in s[2:]:
                    viki_word_count += len(msg)

    print('allen说了', allen_word_count, '个字')
    print('allen发了', allen_sticker_count, '个贴图')
    print('allen发了', allen_image_count, '个字')

    print('viki说了', viki_word_count, '个字')
    print('viki发了', viki_sticker_count, '个贴图')
    print('viki发了', viki_image_count, '个字')

    return chat


# 输出
def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line)


# 合成main
def main():
    lines = read_file('LINE-Viki.txt')

    chat = convert(lines)

    # write_file('output.txt', chat)


main()