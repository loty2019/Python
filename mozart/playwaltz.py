import stdaudio
import stdio
import sys

# Read the waltz measures from standard input into a 1D list.
measures = stdio.readAllInts()

# If the number of measures is not 32, exit with the message
# “A waltz must contain exactly 32 measures”.
if len(measures) != 32:
    sys.exit("A waltz must contain exactly 32 measures")

#  If a minuet measure is not from [1, 176]
#  exit with the message “A minuet measure must be from [1, 176]”.
for i in range(16):
    if 1 > measures[i] > 176:
        sys.exit("A minuet measure must be from [1, 176]")

#  If a trio measure is not from [1, 96],
#  exit with the message “A trio measure must be from [1, 96]”.
for i in range(16, 32):
    if 1 > measures[i] > 96:
        sys.exit("A trio measure must be from [1, 96]")

# Play each of the first 16 minuet and then trio
for i in range(16):
    file = "data/M" + str(measures[i])
    stdaudio.playFile(file)
for i in range(16, 32):
    file = "data/T" + str(measures[i])
    stdaudio.playFile(file)
