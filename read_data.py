#viljum lesa 3 línur í temp.txt og prenta beint út óbreyttar

# open file

def open_file(filename):
    file_object = open(filename, "r")   #"r" = open on read, not writing
    return file_object

# read file

def read_file(file_object, out_object):
    for line in file_object:
        line = line.strip()
        print(line)
        print(line, file=out_object)

# output data

def main():
    # Get filename from user
    filename = input("Enter filename: ")
    file_object = open_file(filename)
    out_object = open("out.txt", "w") #býr til nýja skrá þar sem við sendum out út í 
    read_file(file_object, out_object)

main()