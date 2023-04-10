import math
import stdio


# Entry point.
def main():
    # Initialize ETA, RHO, T, and R to appropriate values
    ETA = 9.135E-4
    RHO = 0.5E-6
    T = 297
    R = 8.31457

    # Calculate var as the sum of the squares of the n displacements each
    # converted from pixels to meters
    var = 0
    displacements = stdio.readAllFloats()
    for i in displacements:
        var += (i * 0.175E-6) ** 2

    # Divide var by 2 * n.
    var = var / (2 * len(displacements))

    # Estimate Boltzmann’s constant as 6 * math.pi * var * ETA * RHO / T
    k = 6 * math.pi * var * ETA * RHO / T

    # Estimate Avogadro’s constant as R / k
    Na = R / k

    # Write to standard output the two constants in scientific notation
    stdio.writef("%e %e\n", k, Na)


if __name__ == '__main__':
    main()
