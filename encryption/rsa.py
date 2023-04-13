import stdio
import stdrandom
import sys


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    # Get a list of primes from the interval lo hi exlusive
    # Sample two distinct random primes p and q from that list
    a = _sample(_primes(lo, hi), 2)
    p, q = a[0], a[1]

    # Set n to pq and m to (p − 1)(q − 1)
    n = p * q
    m = (p - 1) * (q - 1)

    # Loop to make sure e, prime number chosen does not divide m
    e = m
    while m % e == 0:
        # Get a random prime e from a list of primes from the interval [2, m)
        e = _choice(_primes(2, m))

    # Find a d in range [1, m) such that ed mod m = 1
    for i in range(1, m):
        if (e * i) % m == 1:
            d = i
            break

    # Return  tuple (n, e, d).
    t = (n, e, d)
    return t


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    # carry out equation E(x) = x**e mod n and return result
    return x ** e % n


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    # # carry out equation D(y) = y**d mod n and return result
    return y ** d % n


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, '0%db' % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    # Create an empty list to store the primes in
    a = []
    # For each prime from lo to hi, if prime ad to list
    for p in range(lo, hi):
        i = 2
        if p > 1:  # Always start checking after 1 since 0,1 are not primes
            primality = True  # assume p is prime
            # Check if p is prime
            while i <= p / 2:
                if p % i == 0:
                    # Is p is not prime primality = false and stop checking
                    primality = False
                    break
                i += 1
            # If the loop gets exhausted completely then add p to a
            if primality:
                a += [p]

    # Return the list of prime from lo to hi
    return a


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    # Create a copy of a
    b = a[:]

    # Shuffle the first k elements of b
    for i in range(k):
        index = stdrandom.uniformInt(0, len(a))
        b[i], b[index] = b[index], b[i]

    # Return the first k indexes of the shuffled list
    return b[:k]


# Returns a random item from the list a.
def _choice(a):
    # Get a random number r from the list a
    r = stdrandom.uniformInt(0, len(a))

    # Return the element in a at the index r
    return a[r]


# Unit tests the library.
def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))


if __name__ == '__main__':
    _main()
