import math
import stdio
import sys

# accept r (float) and h (float) as command line inputs
r = float(sys.argv[1])
h = float(sys.argv[2])

# carry out equaltions to calculate S surface and V volume
S = 2 * math.pi * r * (r + h)
V = math.pi * (r * r) * h

# write V and S to standard output
stdio.writeln("S = " + str(S) + "\nV = " + str(V))
