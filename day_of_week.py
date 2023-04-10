import stdio
import sys

# Accept m (int) and d (int) y (int) as command-line arguments.
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# Set Y, X, M, dow based on the equations provided.
Y = y - (14 - m) // 12
X = Y + Y // 4 - Y//100 + Y//400
M = m + 12 * ((14 - m) // 12) - 2
dow = (d + X + 31 * M // 12) % 7

# Write dow to standard output.
stdio.writeln(dow)
