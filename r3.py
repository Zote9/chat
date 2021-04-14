
lines= []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())
allen_word_count = 0
viki_word_count = 0

for line in lines:
    s = line.split(' ')
    time = s[0][:5]
    name = s[0][5:]
    for word in s[1:]:
        if name == 'Allen':
            allen_word_count += len(word)
        elif name == 'Viki':
            viki_word_count += len(word)
print('Aleen說了 %s 個字' % allen_word_count)
print('Viki說了 %s 個字' % viki_word_count)
        