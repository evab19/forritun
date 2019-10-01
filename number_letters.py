#Skrifið forrit sem skrifar út hversu oft tiltekinn stafur kemur fyrir í tiltekinni skrá.
#Og í hversu mörgum orðum stafurinn kemur fyrir.
#Ekki skal gera greinarumun á há- og lágstöfum.
#Bæði stafurinn og skráarnafnið eru slegin inn af notanda

# 1. lesa skráarnafn frá notanda

def read_filename():
    name = input("Enter a filename: ")
    return name

# 2. lesa staf frá notanda

def read_char():
    ch = input("Enter a single character: ")
    return ch

# 2.5 Opna skrá

def open_file(filename):
    file_object = open(filename, "r")
    return file_object

# 3. meðhöndla skrá - lesa línu fyrir línu og greint hversu oft stafurinn kemur fyrir í línu og orðum

def count_ch_in_word(user_ch, word):
    counter = 0
    for ch in word:
        if ch == user_ch:
            counter += 1
    return counter


def process_file(file_object, ch):
    #Lesa skrá línu fyrir línu
    ch_count = 0
    word_count = 0
    for line in file_object:
        word_list = line.split() #skilar lista af orðum fyrir sérhverja línu 
        print(word_list)
        for word in word_list:
            count_in_word = count_ch_in_word(ch, word)
            ch_count += count_in_word
            if count_in_word > 0:
                word_count += 1
    #   Telja hversu oft stafur kemur fyrir í skjali
    return ch_count, word_count #skila túplu
# 4. Prenta út upplýsingar fyrir notandann

def print_results(ch, ch_count, word_count):
    print("The letter {} appears {} times".format(ch, ch_count))
    print("The letter {} appears in {} words".format(ch, word_count))

def main():
    filename = read_filename()

    ch = read_char()

    file_object = open_file(filename)

    ch_count, word_count = process_file(file_object, ch)

    print_results(ch, ch_count, word_count)

main()