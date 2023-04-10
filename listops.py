# Returns True if any value in the list a is True, and False otherwise.
def any(a):
    for i in range(len(a)):  # check for the whole length of the list
        if a[i]:
            return True  # check if the value at position i is true,return true and brake the loop
    return False  # if no true value is found return false


# Returns True if all values in the list a are True, and False otherwise.
def all(a):
    for i in range(len(a)):  # check for the whole length of the list
        if not a[i]:
            return False   # if the value at position i is false then return False, break loop
    return True  # if no false are encountered then return true


# Returns True if exactly k values in the list a are True, and False otherwise.
def exactly(a, k):
    nvalue = 0  # to count the number of true
    for i in range(len(a)):  # check for the whole length of the list
        if a[i]:
            nvalue += 1  # if a true is find +1 to the count
        if nvalue > k:   # if there are more true values than k then brake the loop
            return False

    # check if the number of trues matches k
    if nvalue == k:
        return True
    else:
        return False


# Returns the number of True values in the list a.
def count(a):
    ntrue = 0   # to count the number of true
    for i in range(len(a)):  # check for the whole length of the list
        if a[i]:
            ntrue += 1  # if a true is encountered then +1 the count
    return ntrue  # return the total number of true found


# Unit tests the library.
def _main():
    import stdio

    a = [False, False, True, False, True, True, True]
    stdio.writeln('a             = ' + str(a))
    stdio.writeln('any(a)        = ' + str(any(a)))
    stdio.writeln('all(a)        = ' + str(all(a)))
    stdio.writeln('exactly(a, 3) = ' + str(exactly(a, 3)))
    stdio.writeln('count(a)      = ' + str(count(a)))


if __name__ == '__main__':
    _main()
