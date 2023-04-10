import rsa
import stdio
import sys


# Entry point.
def main():
    # Accept private-key n (int) and d (int) as command-line arguments
    n = int(sys.argv[1])
    d = int(sys.argv[2])

    # Accept message from standard input
    e_message = stdio.readString()

    # Get the number of bits per character
    width = rsa.bitLength(n)

    # Get the length of the message
    length = len(e_message)

    for i in range(0, length - 1, width):
        # Set s to substring of message from i to i + width
        s = e_message[i:i+width]

        # Set y to decimal representation of the binary string s.
        y = rsa.bin2dec(s)

        # Decrypt y then write the character corresponding to the decrypted value
        stdio.write(chr(rsa.decrypt(y, n, d)))


if __name__ == '__main__':
    main()
