# Modules
import os
import csv
# get path for election_data.csv
csvpath = os.path.join('Resources', 'election_data.csv')
# open election_data.csv
with open(csvpath, 'r') as csvfile:
    # load election_data.csv int ovar reader
    reader = csv.reader(csvfile, delimiter=',')
    # print out election_data.csv line by line
    csvheader = next(reader)
    # initniate varible
    global khan_count, correy_count, li_count, otooley_count, total
    # set everything to 0
    khan_count = 0
    correy_count = 0
    li_count = 0
    otooley_count = 0
    total = 0
    # as looping through the lines in election_data.csv
    for row in reader:
        # Add 1 into total count
        total += 1
        # if row 3 match "Khan"
        if row[2] == "Khan":
            # add 1 into khan_count
            khan_count += 1
        # if row 3 match "Correy"
        elif row[2] == "Correy":
            # add 1 into correy_count
            correy_count +=1
        # if row 3 match "Li"
        elif row[2] == "Li":
            # add 1 into li_count
            li_count += 1
        # if row 3 match "O'Tooley"
        elif row[2] == "O'Tooley":
            otooley_count += 1

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes : {total}") 
    print(f"Khan: {round(khan_count/total*100,3)}% ({khan_count})")
    print(f"Correy: {round(correy_count/total*100,3)}% ({correy_count})")
    print(f"Li: {round(li_count/total*100,3)}% ({li_count})")
    print(f"O'Tooley: {round(otooley_count/total*100,3)}% ({otooley_count})")
    print("-------------------------")
    # Find highest vote count
    winner_count = max(khan_count, correy_count, li_count, otooley_count)

    if winner_count == khan_count:
        winner_name = "Khan"
    elif winner_count == correy_count:
        winner_name = "Correy"
    elif winner_count == li_count:
        winner_name = "Li"
    elif winner_count == otooley_count:
        winner_name = "O'Tooley"
    
    print(f"The winner is {winner_name}") 
    print("-------------------------")

    
