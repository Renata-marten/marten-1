word = input("Введите искомое слово\n")
w_count = 0
with open("text.txt", encoding='utf-8') as myFile:
    for line in myFile:
        punct_chars = [';', ':', '!' ,'.', ',']
        for i in punct_chars:
            line = line.replace(i, '')
        w_list = line.split()
        w_count += w_list.count(word)
print(w_count)