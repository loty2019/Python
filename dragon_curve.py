import stdio
import sys

# Accept n (int) as command-line argument.
n = int(sys.argv[1])

# set dragon and nogard to teh string F
dragon = str("F")
nogard = str("F")

# For each value of i from [1, n], exchange dragon with dragon "L"
# nogard and nogard with dragon "R" nogard
for i in range(1, n+1):
    dragon, nogard = dragon + "L" + nogard, dragon + "R" + nogard

# write dragon to standard output
stdio.writeln(dragon)
