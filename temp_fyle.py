
temp_file = open("temp.txt", "w") #creates a file if it doesn't exist
print("first line", file=temp_file)
print("second line", file=temp_file)
temp_file.close()