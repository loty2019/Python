import stdio
import stdrandom

# Set rank to a random integer from [2, 15]
rank = stdrandom.uniformInt(2, 15)

# make rankStr to be the string version of rank
if rank == 2:
    rankStr = "2"
if rank == 3:
    rankStr = "3"
if rank == 4:
    rankStr = "4"
if rank == 5:
    rankStr = "5"
if rank == 6:
    rankStr = "6"
if rank == 7:
    rankStr = "7"
if rank == 8:
    rankStr = "8"
if rank == 9:
    rankStr = "9"
if rank == 10:
    rankStr = "10"
if rank == 11:
    rankStr = "Jack"
if rank == 12:
    rankStr = "Queen"
if rank == 13:
    rankStr = "King"
if rank == 14:
    rankStr = "Ace"

# Set suit to a random integer from [1, 5]
suit = stdrandom.uniformInt(1, 5)

# Make suitStr be the suits in str
if suit == 1:
    suitStr = "Clubs"
if suit == 2:
    suitStr = "Diamonds"
if suit == 3:
    suitStr = "Hearts"
if suit == 4:
    suitStr = "Spades"
# Write rankStr of suitStr to standard output.
stdio.writeln(rankStr + " of " + suitStr)
