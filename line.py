
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    name = None
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[2:]
        name = s[1]
        for word in s[2:]:
            if name == 'Allen':
                if s[2] == '貼圖':
                    allen_sticker_count += 1
                elif s[2] == '圖片':
                    allen_image_count += 1
                else:
                    allen_word_count += len(word)
            elif name == "Viki":
                if s[2] == '貼圖':
                    viki_sticker_count += 1
                elif s[2] == '圖片':
                    viki_image_count += 1
                else:
                    viki_word_count += len(word)
    print('Allen 說了 %s 個字,傳了 %s 個貼圖, 傳了 %s 張圖片' % \
        (allen_word_count, allen_sticker_count, allen_image_count))
    print('viki 說了 %s 個字,傳了 %s 個貼圖, 傳了 %s 張圖片' % \
        (viki_word_count, viki_sticker_count, viki_image_count))
    
    # return new


def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    # write_file('convert_line.txt', lines)
main()