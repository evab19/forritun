#open the file for reading
file_str = input("Enter a file name: ")

while True: #loop until you break
    try: 
        poker_file = open(file_str, "r")
        break
    except IOError: #if the file doesn't exist
        print("Error opening the file", file_str)
        file_str = input("Enter a file name: ")

#create variables to hold our counts and set them to zero
total_count = 0
pair_count = 0


#loop through the file reading one line at a time

for line in poker_file:
    total_count += 1 #add 1 to our counter for every line

    fields = line.split(",") #split the lines up with the commas
    hand_rank = fields[-1] #get the last item (index -1)
    hand_rank_int = int(hand_rank)
    
    if hand_rank_int == 1:
        pair_count += 1#if hand ranks 1, then add one to our pair counter

odds_of_pair = pair_count / total_count

print("Total count is ", total_count)
print("Count of pair hands: ", pair_count)
print("The odds: {:%}".format(odds_of_pair)) #the formatting takes the float and prints it as a %