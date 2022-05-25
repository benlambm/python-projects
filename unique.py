def main():
    unique_words = []
    file_name = input("Enter the input file name: ")
    fio = open(file_name, 'r')
    lines = fio.readlines()
    all_words = []
    for line in lines:
        temp_line = line.strip()
        for word in temp_line.split(' '):
            all_words.append(word)
            if word in unique_words:
                continue
            else:
                unique_words.append(word)
    unique_words.sort()
    for word in unique_words:
        print(word, + all_words.count(word))


main()