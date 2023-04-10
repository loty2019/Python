import stdarray
import stdrandom
import stdio

# Read the minuet measures from standard input into a 2D list with dimensions 11 × 16.
Minuet = stdarray.create2D(11, 16)
for i in range(11):
    for j in range(16):
        Minuet[i][j] = stdio.readInt()

# Read the trio measures from standard input into a 2D list with dimensions 6 × 16.
Trio = stdarray.create2D(6, 16)
for i in range(6):
    for j in range(16):
        Trio[i][j] = stdio.readInt()

# Write to standard output a random sequence of 16 minuet measures
for measures in range(16):
    i = stdrandom.uniformInt(1, 7) + stdrandom.uniformInt(1, 7) - 2
    while i > 10:
        i = stdrandom.uniformInt(1, 7) + stdrandom.uniformInt(1, 7) - 2
    j = stdrandom.uniformInt(0, 16)
    stdio.write(str(Minuet[i][j]) + " ")

# Write to standard output a random sequence of 16 trio measures
for measures in range(16):
    i = stdrandom.uniformInt(0, 6)
    j = stdrandom.uniformInt(0, 16)
    stdio.write(str(Trio[i][j]) + " ")
stdio.writeln()
