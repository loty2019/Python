import stdio
import sys

# Accept n (int) as command-line argument.
n = int(sys.argv[1])

# set a equal to 1
a = 1

# as long as a^3 <= n
while a*a*a <= n:
    b = a+1
    while b*b*b <= n-a*a*a:  # as long as b^3 <= n-a^3
        c = a+1
        while c*c*c <= n:  # as long as c^3 <= n
            d = c+1
            while d*d*d <= n-c*c*c:   # as long as d^3 <= n-c^3

                # check if the sum of the cubes is the same
                if a*a*a + b*b*b == c*c*c + d*d*d:

                    # Write the sum of qubes to standard output.
                    stdio.write(str(a*a*a + b*b*b) + " = ")
                    stdio.write(str(a) + "^3 + " + str(b) + "^3 = ")
                    stdio.writeln(str(c) + "^3 + " + str(d) + "^3")
                d += 1
            c += 1
        b += 1
    a += 1
