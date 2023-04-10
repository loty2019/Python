import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    # Accept command-line arguments pixels (int), tau (float), and delta (float)
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])

    # Construct a BlobFinder object for the frame sys.argv[4] and from it get a list of beads
    # prevBeads that have at least pixels pixels
    prevBeats = BlobFinder(Picture(sys.argv[4]), tau).getBeads(pixels)

    # Construct a BlobFinder object and from it get a list of beads currBeads that have at
    # least pixels pixels
    for i in sys.argv[5:]:
        currBeads = BlobFinder(Picture(i), tau).getBeads(pixels)

        # For each bead currBead in currBeads, find a bead prevBead from prevBeads that is
        # no further than delta and is closest to currBead, and if such a bead is found,
        # write its distance to currBead
        for currBead in currBeads:
            closest = math.inf
            for prevBeat in prevBeats:
                r = currBead.distanceTo(prevBeat)
                if r <= delta and r < closest:
                    closest = r
            if closest != math.inf:
                stdio.writef("%.4f\n", closest)

        # Write a newline character and set prevBeads to currBeads.
        stdio.writeln()
        prevBeats = currBeads


if __name__ == '__main__':
    main()
