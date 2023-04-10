import stdio
import sys

# Accept n (int) as command-line argument.
n = int(sys.argv[1])

# set a=1 b=1 i=3
a, b = 1, 1
i = 3

# as long as i<=n exchange a with b and b with a+b
while i <= n:
    a, b = b, a+b
    i += 1

# Write b to standard output
stdio.writeln(b)
