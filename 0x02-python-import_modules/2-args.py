#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    counter = len(sys.argv) - 1
    if counter == 0:
    print("0 arguments.")
    elif count == 1:
    print("1 argument:")
    else:
    print("{} arguments:".format(count))
    for r in range(counter):
    print("{}: {}".format(r + 1, sys.argv[r + 1]))
