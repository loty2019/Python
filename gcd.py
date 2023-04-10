import stdio
import sys

# Accept p (int) and q (int) as command-line argument.
p = int(sys.argv[1])
q = int(sys.argv[2])

# as long as p mod q is different 0, exchange p with q and q with p mod q
while p % q != 0:
    p, q = q, p % q

# write q to standard output
stdio.writeln(q)
