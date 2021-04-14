

def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    new = []
    name = None
    for line in lines:
        if line == 'Allen':
            name = 'Allen'
            continue
        elif line == 'Tom':
            name = 'Tom'
            continue
        if name:
            new.append(name + ': ' + line)
    return new


def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('convert.txt', lines)


main()