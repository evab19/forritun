
def open_file(filename):
  file_object = open(filename, 'r')
  return file_object

def write_sentences(word_file):
    sent_file = open('sentences.txt','w')
    sentence = ''
    for word in word_file:	# process each line/word
        word = word.strip() # strip leading and trailing white space
        if word == '.':  # sentence boundary
            sentence = sentence.strip() + "."
            sent_file.write(sentence+"\n")
            print(sentence)
            sentence = ''
        elif word == ' ':
            continue
        elif  word == ',':
            sentence = sentence.strip() + ', '
        else:
            sentence = sentence + word + ' '

# Main program starts here
filename = input("Enter filename: ")
file_object = open_file(filename)
write_sentences(file_object)
file_object.close()