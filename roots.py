from quadratic import Quadratic
import stdio
import sys


# Entry point.
def main():
    # read a float x as command line argument
    x = float(sys.argv[1])

    # as long as standard input is empty
    while not stdio.isEmpty():
        # read a,b,c as floats
        a = stdio.readFloat()
        b = stdio.readFloat()
        c = stdio.readFloat()

        # construct a quadratic object
        quadratic = Quadratic(a, b, c)

        # write to standard output the quadratic objects and its methods
        stdio.write(quadratic)
        stdio.writef("; %f; ", quadratic.__getitem__(x))
        stdio.write(quadratic.roots())
        stdio.writef("; %f; %f", quadratic.sum(), quadratic.prod())


if __name__ == '__main__':
    main()
