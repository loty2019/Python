import stdio
import sys

# Accept t (float) and v (float) as command-line argument.
t = float(sys.argv[1])
v = float(sys.argv[2])

# if t>50 write "Value of t must be <= 50 F"
if t > 50:
    stdio.writeln("Value of t must be <= 50 F")

else:  # if t<50 but v<=3 then write "Value of v must be > 3 mph"
    if v <= 3:
        stdio.writeln("Value of v must be > 3 mph")

    else:   # if t<50 and v>3 then carry out equation
        w = 35.74 + 0.6215*t + (0.4275*t - 35.75)*v**0.16

        # Write w to standard output.
        stdio.writeln(w)
