import sys


def main():
    print("Thing-Scraper\n")
    opts = getopts(sys.argv)
    print(opts)
    if len(sys.argv) < 2:
        Usage()


def Usage():
    print("USAGE:\n thing-scraper <optional cmd> <page url> \n")

#REF: https://gist.github.com/dideler/2395703
def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            try:
                opts[argv[0]] = argv[1]  # Add key and value to the dictionary. Catch exeption with -command only
            except IndexError:
                Usage()
                sys.exit(1)
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

#Running from the command line
if __name__ == '__main__':
    main()
    