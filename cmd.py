import sys
import re
from logger import log

def main():
    print("thing-scraper\n")
    opts = getopts(sys.argv)
    if len(sys.argv) < 2:
        Usage()
        sys.exit(1)
    parse_opts(opts)
    print('exit')


#Parse command line options and branch to control functionsw
def parse_opts(opts):

    if opts['-s'] != '':
        if verifyURL(opts['-s']):
            log.New('log', 'URL valid').print()
            scrape_url(opts['-s'])
        else: 
            log.New('error', 'URL invalid').print()


def scrape_url(url):
    log.New('log', 'Handling ' + url).print()


# verifyUrl returns true if url matches the regular expression
def verifyURL(url):
    # https://xkcd.com/1171/
    exp = re.compile('(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})')
    if(exp.match(url)):
        return True
    return False
    

# Usage prints usage information
def Usage():
    print("USAGE:\n thing-scraper <optional cmd> <page url> \n")


# REF: https://gist.github.com/dideler/2395703
def getopts(argv):
    opts = {} # Empty dictionary to store key-value pairs.
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
    