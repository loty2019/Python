import stdio
import sys

# Accept n (int) as command-line argument.
n = int(sys.argv[1])

# For each value of i from [2, n], set total to 0
for i in range(2, n+1):
    total = 0

    # For each value of j from [1, i], if i mod j equals 0, set total to its current value plus j
    for j in range(1, i):
        if i % j == 0:
            total += j

    # if total equals i, write i to standard output
    if total == i:
        stdio.writeln(i)
