import stdio
import stdrandom
import sys

# Accept n (int) as command-line arguments.
n = int(sys.argv[1])

# Set total to the sum of two dice rolls.
total = stdrandom.uniformInt(1, n+1) + stdrandom.uniformInt(1, n+1)

# Write total to standard output.
stdio.writeln(total)
