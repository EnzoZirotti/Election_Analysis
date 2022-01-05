#1.Open the data file.
#2.Write down the names of all the candidates.
#3.Add a vote count for each candidate.
#4.Get the total votes for each candidate.
#5.Get the total votes cast for the election.

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Election_Analysis","Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)