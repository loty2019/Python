import stdio
import sys

# Accept x (int),y (int) and z (int) as command-line arguments.
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# Set Mi to the lowest number between x,y and z; set Ma to the highest.
Mi = min(x, y, z)
Ma = max(x, y, z)

# Write p to standard output.
stdio.writeln(str(Mi) + " " + str(x+y+z-Mi-Ma) + " " + str(Ma))
