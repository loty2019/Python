import stdio
import sys

# Accept m (int), d (int) and y (int) as command-line argument.
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# carry out equation for yo, xo, mo and dow
yo = y - (14-m)//12
xo = yo + yo//4 - yo//100 + yo//400
mo = m + 12 * ((14-m)//12) - 2
dow = (d + xo + 31 * mo//12) % 7

# Correspond dow to the day of the week with 0 being Sunday and write it to standard output
if dow == 0:
    stdio.writeln("Sunday")
if dow == 1:
    stdio.writeln("Monday")
if dow == 2:
    stdio.writeln("Tuesday")
if dow == 3:
    stdio.writeln("Wednesday")
if dow == 4:
    stdio.writeln("Thursday")
if dow == 5:
    stdio.writeln("Friday")
if dow == 6:
    stdio.writeln("Saturday")
