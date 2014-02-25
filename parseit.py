import argparse

__author__ = 'souriyakhaosanga'


def main():
    #Used to echo the system args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("echo")
    args = parser.parse_args()

    print args.echo
    """

    #pretty much square function where the type is set to integer
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display a square of a given number",type=int)
    args = parser.parse_args()
    print pow(args.square, 2)
    """

    #optional arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbosity", help="increase output verbosity")
    args = parser.parse_args()
    if args.verbosity:
        print "verbosity turned on"
        print args.verbosity
    else:
        print "its not on"
    """

    #Short Options that means -v and --verbose
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
    args = parser.parse_args()
    if args.verbose:
        print "verbosity turned on"
    '''


if __name__ == "__main__":
    main()