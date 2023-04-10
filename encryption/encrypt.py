import rsa
import stdio
import sys


# Entry point.
def main():
    # Accept public-key n (int) and e (int) as command-line arguments
    n = int(sys.argv[1])
    e = int(sys.argv[2])

    # Accept the message to encrypt from standard input
    message = stdio.readAll()

    # Get the number of bits per character
    width = rsa.bitLength(n)

    # For each word  w in message and for each character c in word
    for w in message:
        for c in w:
            # Turn c into an integer, encrypt it and
            # then write the encrypted value as a width-long binary string
            stdio.write(rsa.dec2bin(rsa.encrypt(ord(c), n, e), width))

    # Write a newline character
    stdio.writeln()


if __name__ == '__main__':
    main()
