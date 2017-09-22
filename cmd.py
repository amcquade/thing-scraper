import sys
import re

def main():
    print("thing-scraper\n")
    opts = getopts(sys.argv)
    if len(sys.argv) < 2:
        Usage()
        sys.exit(1)
    parse_opts(opts)
    print('exit')


#Parse command line options and branch to control functions
def parse_opts(opts):

    if opts['-s'] != '':
        if verifyURL(opts['-s']):
            Log('log', 'URL valid').print()
            scrape_url(opts['-s'])
        else: 
            Log('error', 'URL invalid').print()

def scrape_url(url):
    Log('log', 'Handling ' + url).print()

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


#REF: https://gist.github.com/dideler/2395703
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

class Log:
    def __init__(self, err_type, message):
        self._error_types = 'error', 'warning', 'log'
        try:
            self._check_type(err_type)
        except TypeError:
            print('Invalid error of type: ' + err_type + '\n')
        err_type = err_type.upper()
        self._type = err_type
        self._message = message

    def _check_type(self, err_type):
        for t in self._error_types:
            if err_type == t:
                return
        raise TypeError

    def print(self):
        print('[' + self._type + ']: ' + self._message + '\n')
        if self._type == 'ERROR':
            print('exiting...\n')


#Running from the command line
if __name__ == '__main__':
    main()
    